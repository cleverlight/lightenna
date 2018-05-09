
/**
 * Override jQuery.fn.init to guard against XSS attacks.
 *
 * See http://bugs.jquery.com/ticket/9521
 */
(function () {
  var jquery_init = jQuery.fn.init;
  jQuery.fn.init = function (selector, context, rootjQuery) {
    // If the string contains a "#" before a "<", treat it as invalid HTML.
    if (selector && typeof selector === 'string') {
      var hash_position = selector.indexOf('#');
      if (hash_position >= 0) {
        var bracket_position = selector.indexOf('<');
        if (bracket_position > hash_position) {
          throw 'Syntax error, unrecognized expression: ' + selector;
        }
      }
    }
    return jquery_init.call(this, selector, context, rootjQuery);
  };
  jQuery.fn.init.prototype = jquery_init.prototype;
})();

var Drupal = Drupal || { 'settings': {}, 'behaviors': {}, 'themes': {}, 'locale': {} };

/**
 * Set the variable that indicates if JavaScript behaviors should be applied
 */
Drupal.jsEnabled = document.getElementsByTagName && document.createElement && document.createTextNode && document.documentElement && document.getElementById;

/**
 * Attach all registered behaviors to a page element.
 *
 * Behaviors are event-triggered actions that attach to page elements, enhancing
 * default non-Javascript UIs. Behaviors are registered in the Drupal.behaviors
 * object as follows:
 * @code
 *    Drupal.behaviors.behaviorName = function () {
 *      ...
 *    };
 * @endcode
 *
 * Drupal.attachBehaviors is added below to the jQuery ready event and so
 * runs on initial page load. Developers implementing AHAH/AJAX in their
 * solutions should also call this function after new page content has been
 * loaded, feeding in an element to be processed, in order to attach all
 * behaviors to the new content.
 *
 * Behaviors should use a class in the form behaviorName-processed to ensure
 * the behavior is attached only once to a given element. (Doing so enables
 * the reprocessing of given elements, which may be needed on occasion despite
 * the ability to limit behavior attachment to a particular element.)
 *
 * @param context
 *   An element to attach behaviors to. If none is given, the document element
 *   is used.
 */
Drupal.attachBehaviors = function(context) {
  context = context || document;
  if (Drupal.jsEnabled) {
    // Execute all of them.
    jQuery.each(Drupal.behaviors, function() {
      this(context);
    });
  }
};

/**
 * Encode special characters in a plain-text string for display as HTML.
 */
Drupal.checkPlain = function(str) {
  str = String(str);
  var replace = { '&': '&amp;', '"': '&quot;', '<': '&lt;', '>': '&gt;' };
  for (var character in replace) {
    var regex = new RegExp(character, 'g');
    str = str.replace(regex, replace[character]);
  }
  return str;
};

/**
 * Translate strings to the page language or a given language.
 *
 * See the documentation of the server-side t() function for further details.
 *
 * @param str
 *   A string containing the English string to translate.
 * @param args
 *   An object of replacements pairs to make after translation. Incidences
 *   of any key in this array are replaced with the corresponding value.
 *   Based on the first character of the key, the value is escaped and/or themed:
 *    - !variable: inserted as is
 *    - @variable: escape plain text to HTML (Drupal.checkPlain)
 *    - %variable: escape text and theme as a placeholder for user-submitted
 *      content (checkPlain + Drupal.theme('placeholder'))
 * @return
 *   The translated string.
 */
Drupal.t = function(str, args) {
  // Fetch the localized version of the string.
  if (Drupal.locale.strings && Drupal.locale.strings[str]) {
    str = Drupal.locale.strings[str];
  }

  if (args) {
    // Transform arguments before inserting them
    for (var key in args) {
      switch (key.charAt(0)) {
        // Escaped only
        case '@':
          args[key] = Drupal.checkPlain(args[key]);
        break;
        // Pass-through
        case '!':
          break;
        // Escaped and placeholder
        case '%':
        default:
          args[key] = Drupal.theme('placeholder', args[key]);
          break;
      }
      str = str.replace(key, args[key]);
    }
  }
  return str;
};

/**
 * Format a string containing a count of items.
 *
 * This function ensures that the string is pluralized correctly. Since Drupal.t() is
 * called by this function, make sure not to pass already-localized strings to it.
 *
 * See the documentation of the server-side format_plural() function for further details.
 *
 * @param count
 *   The item count to display.
 * @param singular
 *   The string for the singular case. Please make sure it is clear this is
 *   singular, to ease translation (e.g. use "1 new comment" instead of "1 new").
 *   Do not use @count in the singular string.
 * @param plural
 *   The string for the plural case. Please make sure it is clear this is plural,
 *   to ease translation. Use @count in place of the item count, as in "@count
 *   new comments".
 * @param args
 *   An object of replacements pairs to make after translation. Incidences
 *   of any key in this array are replaced with the corresponding value.
 *   Based on the first character of the key, the value is escaped and/or themed:
 *    - !variable: inserted as is
 *    - @variable: escape plain text to HTML (Drupal.checkPlain)
 *    - %variable: escape text and theme as a placeholder for user-submitted
 *      content (checkPlain + Drupal.theme('placeholder'))
 *   Note that you do not need to include @count in this array.
 *   This replacement is done automatically for the plural case.
 * @return
 *   A translated string.
 */
Drupal.formatPlural = function(count, singular, plural, args) {
  var args = args || {};
  args['@count'] = count;
  // Determine the index of the plural form.
  var index = Drupal.locale.pluralFormula ? Drupal.locale.pluralFormula(args['@count']) : ((args['@count'] == 1) ? 0 : 1);

  if (index == 0) {
    return Drupal.t(singular, args);
  }
  else if (index == 1) {
    return Drupal.t(plural, args);
  }
  else {
    args['@count['+ index +']'] = args['@count'];
    delete args['@count'];
    return Drupal.t(plural.replace('@count', '@count['+ index +']'), args);
  }
};

/**
 * Generate the themed representation of a Drupal object.
 *
 * All requests for themed output must go through this function. It examines
 * the request and routes it to the appropriate theme function. If the current
 * theme does not provide an override function, the generic theme function is
 * called.
 *
 * For example, to retrieve the HTML that is output by theme_placeholder(text),
 * call Drupal.theme('placeholder', text).
 *
 * @param func
 *   The name of the theme function to call.
 * @param ...
 *   Additional arguments to pass along to the theme function.
 * @return
 *   Any data the theme function returns. This could be a plain HTML string,
 *   but also a complex object.
 */
Drupal.theme = function(func) {
  for (var i = 1, args = []; i < arguments.length; i++) {
    args.push(arguments[i]);
  }

  return (Drupal.theme[func] || Drupal.theme.prototype[func]).apply(this, args);
};

/**
 * Parse a JSON response.
 *
 * The result is either the JSON object, or an object with 'status' 0 and 'data' an error message.
 */
Drupal.parseJson = function (data) {
  if ((data.substring(0, 1) != '{') && (data.substring(0, 1) != '[')) {
    return { status: 0, data: data.length ? data : Drupal.t('Unspecified error') };
  }
  return eval('(' + data + ');');
};

/**
 * Freeze the current body height (as minimum height). Used to prevent
 * unnecessary upwards scrolling when doing DOM manipulations.
 */
Drupal.freezeHeight = function () {
  Drupal.unfreezeHeight();
  var div = document.createElement('div');
  $(div).css({
    position: 'absolute',
    top: '0px',
    left: '0px',
    width: '1px',
    height: $('body').css('height')
  }).attr('id', 'freeze-height');
  $('body').append(div);
};

/**
 * Unfreeze the body height
 */
Drupal.unfreezeHeight = function () {
  $('#freeze-height').remove();
};

/**
 * Wrapper around encodeURIComponent() which avoids Apache quirks (equivalent of
 * drupal_urlencode() in PHP). This function should only be used on paths, not
 * on query string arguments.
 */
Drupal.encodeURIComponent = function (item, uri) {
  uri = uri || location.href;
  item = encodeURIComponent(item).replace(/%2F/g, '/');
  return (uri.indexOf('?q=') != -1) ? item : item.replace(/%26/g, '%2526').replace(/%23/g, '%2523').replace(/\/\//g, '/%252F');
};

/**
 * Get the text selection in a textarea.
 */
Drupal.getSelection = function (element) {
  if (typeof(element.selectionStart) != 'number' && document.selection) {
    // The current selection
    var range1 = document.selection.createRange();
    var range2 = range1.duplicate();
    // Select all text.
    range2.moveToElementText(element);
    // Now move 'dummy' end point to end point of original range.
    range2.setEndPoint('EndToEnd', range1);
    // Now we can calculate start and end points.
    var start = range2.text.length - range1.text.length;
    var end = start + range1.text.length;
    return { 'start': start, 'end': end };
  }
  return { 'start': element.selectionStart, 'end': element.selectionEnd };
};

/**
 * Build an error message from ahah response.
 */
Drupal.ahahError = function(xmlhttp, uri) {
  if (xmlhttp.status == 200) {
    if (jQuery.trim($(xmlhttp.responseText).text())) {
      var message = Drupal.t("An error occurred. \n@uri\n@text", {'@uri': uri, '@text': xmlhttp.responseText });
    }
    else {
      var message = Drupal.t("An error occurred. \n@uri\n(no information available).", {'@uri': uri, '@text': xmlhttp.responseText });
    }
  }
  else {
    var message = Drupal.t("An HTTP error @status occurred. \n@uri", {'@uri': uri, '@status': xmlhttp.status });
  }
  return message;
}

// Global Killswitch on the <html> element
if (Drupal.jsEnabled) {
  // Global Killswitch on the <html> element
  $(document.documentElement).addClass('js');
  // 'js enabled' cookie
  document.cookie = 'has_js=1; path=/';
  // Attach all behaviors.
  $(document).ready(function() {
    Drupal.attachBehaviors(this);
  });
}

/**
 * The default themes.
 */
Drupal.theme.prototype = {

  /**
   * Formats text for emphasized display in a placeholder inside a sentence.
   *
   * @param str
   *   The text to format (plain-text).
   * @return
   *   The formatted text (html).
   */
  placeholder: function(str) {
    return '<em>' + Drupal.checkPlain(str) + '</em>';
  }
};
;

/**
 * @file
 * Enables and disables expiration fields to prevent invalid configurations.
 */

/**
 * Disables duration amount when its type is "never".
 */
function _uc_role_expiration_disable_check(granularity, quantity) {
  // 'never' means there's no point in setting a duration.
  if ($(granularity).val() == 'never') {
    $(quantity).attr('disabled', 'disabled').val('');
  }
  // Anything besides 'never' should enable setting a duration.
  else {
    $(quantity).removeAttr('disabled');
  }
}

/**
 * Switch between relative and absolute expiration durations.
 */
function expiration_switcher() {
  if ($('#edit-expiration').val() == 'abs') {
    $("#edit-uc-roles-expire-relative-duration-wrapper").hide();
    $("#edit-uc-roles-expire-relative-granularity-wrapper").hide();
    $("#edit-uc-roles-by-quantity-wrapper").hide();
    $("#edit-uc-roles-expire-absolute-wrapper").show();
  }
  else {
    $("#edit-uc-roles-expire-absolute-wrapper").hide();
    $("#edit-uc-roles-expire-relative-duration-wrapper").show();
    $("#edit-uc-roles-expire-relative-granularity-wrapper").show();
    $("#edit-uc-roles-by-quantity-wrapper").show();
  }
}

/**
 * Set the default state for expiration duration.
 */
function expiration_switcher_default() {
  if ($('#edit-uc-roles-default-end-expiration').val() == 'abs') {
    $("#edit-uc-roles-default-length-wrapper").attr('style', 'display:none;');
    $("#edit-uc-roles-default-granularity-wrapper").attr('style', 'display:none;');
    $("#edit-uc-roles-default-by-quantity-wrapper").attr('style', 'display:none;');
    $("#edit-uc-roles-default-end-time-wrapper").removeAttr('style');
  }
  else {
    $("#edit-uc-roles-default-length-wrapper").removeAttr('style');
    $("#edit-uc-roles-default-granularity-wrapper").removeAttr('style');
    $("#edit-uc-roles-default-by-quantity-wrapper").removeAttr('style');
    $("#edit-uc-roles-default-end-time-wrapper").attr('style', 'display:none;');
  }
}

/**
 * Override the expiration duration default state.
 */
function uc_roles_expiration_default_override() {
  if ($('#edit-end-override').length == 0) {
    return;
  }

  if ($('#edit-end-override').attr('checked')) {
    $('#edit-expiration-wrapper').removeAttr('style');
    $('#edit-uc-roles-expire-absolute-wrapper').removeAttr('style');
    $('#edit-uc-roles-expire-relative-duration-wrapper').removeAttr('style');
    $('#edit-uc-roles-expire-relative-granularity-wrapper').removeAttr('style');
    $('#edit-uc-roles-by-quantity-wrapper').removeAttr('style');
    expiration_switcher();
  }
  else {
    $('#edit-expiration-wrapper').attr('style', 'display:none;');
    $('#edit-uc-roles-expire-relative-duration-wrapper').attr('style', 'display:none;');
    $('#edit-uc-roles-expire-relative-granularity-wrapper').attr('style', 'display:none;');
    $('#edit-uc-roles-by-quantity-wrapper').attr('style', 'display:none;');
    $('#edit-uc-roles-expire-absolute-wrapper').attr('style', 'display:none;');
  }
}

$(document).ready(
  function() {
    _uc_role_expiration_disable_check('#edit-uc-roles-expire-relative-granularity', '#edit-uc-roles-expire-relative-duration');
    _uc_role_expiration_disable_check('#edit-uc-roles-default-granularity', '#edit-uc-roles-default-length');
    _uc_role_expiration_disable_check('#edit-uc-roles-reminder-granularity', '#edit-uc-roles-reminder-length');
    uc_roles_expiration_default_override();
    expiration_switcher_default();
  }
);

// When you change the role expiration time select.
Drupal.behaviors.ucRoleExpirationTime = function(context) {
  $("#edit-expiration:not(.ucRoleExpirationTime-processed)", context).addClass('ucRoleExpirationTime-processed').change(
    function() {
      expiration_switcher();
    }
  );
}

// When you change the default role expiration time select.
Drupal.behaviors.ucRoleDefaultExpirationTimeDefault = function(context) {
  $("#edit-uc-roles-default-end-expiration:not(.ucRoleDefaultExpirationTimeDefault-processed)", context).addClass('ucRoleDefaultExpirationTimeDefault-processed').change(
    function() {
      expiration_switcher_default();
    }
  );
}

// When you change the role expiration time select.
Drupal.behaviors.ucRoleExpirationTimeDefault = function(context) {
  $("#edit-uc-roles-end-expiration:not(.ucRoleExpirationTimeDefault-processed)", context).addClass('ucRoleExpirationTimeDefault-processed').change(
    function() {
      expiration_switcher_default();
    }
  );
}

// When you change the role expiration granularity select.
Drupal.behaviors.ucRoleExpirationGranularity = function(context) {
  $('#edit-uc-roles-expire-relative-granularity:not(.ucRoleExpirationGranularity-processed)', context).addClass('ucRoleExpirationGranularity-processed').change(
    function() {
      _uc_role_expiration_disable_check('#edit-uc-roles-expire-relative-granularity', '#edit-uc-roles-expire-relative-duration');
    }
  );
}

// When you change the default role expiration granularity select.
Drupal.behaviors.ucRoleDefaultExpirationGranularity = function(context) {
  $('#edit-uc-roles-default-granularity:not(.ucRoleDefaultExpirationGranularity-processed)', context).addClass('ucRoleDefaultExpirationGranularity-processed').change(
    function() {
      _uc_role_expiration_disable_check('#edit-uc-roles-default-granularity', '#edit-uc-roles-default-length');
    }
  );
}

// When you change the default role expiration granularity select.
Drupal.behaviors.ucRoleReminderExpirationGranularity = function(context) {
  $('#edit-uc-roles-reminder-granularity:not(.ucRoleReminderExpirationGranularity-processed)', context).addClass('ucRoleReminderExpirationGranularity-processed').change(
    function() {
      _uc_role_expiration_disable_check('#edit-uc-roles-reminder-granularity', '#edit-uc-roles-reminder-length');
    }
  );
}

// When you change the default role expiration granularity select.
Drupal.behaviors.ucRoleExpirationEndOverride = function(context) {
  $('#edit-end-override:not(.ucRoleExpirationEndOverride-processed)', context).addClass('ucRoleExpirationEndOverride-processed').click(
    function() {
      uc_roles_expiration_default_override();
    }
  );
}

;
/**
 * gmapmark.js
 */

(function($, undefined) {
  window.gmapmark = {
    that : this,

    // google maps object
    gmaps : null,
    // our map
    map : null,
    // our current kmlLayer
    kmlLayer : null,
    // info box
    infot : null,
    // currently selected marker
    marker : null,
    // current map zoom level
    zoomLevel : 0,

    // default path, overwritten by setting
    kmlPath : 'http://gmaps-samples.googlecode.com/svn/trunk/ggeoxml/cta.kml',
    
    // default options for KML layers
    kmlOptions : {
      'preserveViewport' : true,
      'suppressInfoWindows' : true
    },
    
    init : function(m, ms) {
      var scope, that = this, currentFilterTarget, url;
      this.map = m;
      this.gmaps = ms;
      // update zoom level
      that.zoomLevel = that.map.getZoom();
      // listen for resize event
      $(window).resize(that.resize);
      // make non-map columns squishable
      $('div.sidebar').addClass('squishable');
      // create kml layer
      url = this.kmlGetPath();
      // if (console && console.log) console.log(url);
      this.kmlLoadLayer(url);
      // hunt down the info box
      this.infot = $('#gmapmark_kml_info');
      // hunt down the kml links
      scope = $('#gmapmark_kml_links');
      $('a.gmapmark_kml_networklink', scope).click(function(ev) {
        var url, rawurl = ev.target.href;
        // extract the real URL from this non-js safe href
        url = unescape(rawurl.substring(rawurl.indexOf('#') + 1));
        console.log(url);
        // load the new KML layer
        that.kmlLoadLayer(url);
        // clear the active class from the last link
        if (currentFilterTarget) {
          currentFilterTarget.removeClass('active');
        }
        // flag this link as active
        currentFilterTarget = $(ev.target).addClass('active');
        // stop the click travelling any further
        ev.preventDefault();
        return false;
      });
    },

    resize : function() {
      var h = $(window).height();
      // resize main page
      $('div.main_column').height(h - 84);
      // resize all sidebars
      $('div.squishable').height(h - 84 - 30);
    },

    /**
     * @param string url Url of KML layer to load
     */
    kmlLoadLayer : function(url) {
      var that = this, tkml;
      // start the new layer loading
      tkml = new this.gmaps.KmlLayer(url, that.kmlOptions);
      // display as soon as possible
      if (this.kmlLayer) {
        // clear the last KML layer if set
        this.kmlLayer.setMap(null);
      }
      // attach new KML to map
      tkml.setMap(this.map);
      this.kmlLayer = tkml;
      // add a loading listener to the map
      this.gmaps.event.addListener(tkml, "metadata_changed", function() {
      });
      // add a click listener to the KML layer
      this.gmaps.event.addListener(tkml, 'click', this.kmlClickEvent(this));
      // add a zoom listener to the map
      this.gmaps.event.addListener(this.map, 'zoom_changed', this.kmlZoomEvent(this));
    },
    
    /**
     * @param object that Context from caller (this)
     * @return function Click listener for handling KML layer events
     */
    kmlClickEvent : function(that) {
      return function(kmlEvent) {
        var id = kmlEvent.featureData.id, blk, nid, sid;
        // fail if we can't get the marker's ID
        if (!id)
          return;
        blk = kmlEvent.featureData.id.split('-');
        if (blk.length < 4)
          return;
        // extract node id and submission id
        nid = parseInt(blk[1]);
        sid = parseInt(blk[3]);
        // if (console && console.log) console.log('/node/'+nid+'/sub/'+sid);
        // hunt for info block
        if (that.infot.length) {
          // use info pane, insert spinner to show we're loading
          that.infot
              .html('<div class="inuse loading"><img src="/legacy/misc/spinner-big.gif" alt="Loading..." /><br />Loading data</div>');
        } else {
          // augment balloon: create hook id
          id += '-desc';
          // add hook to description
          kmlEvent.featureData.description += '<div id="' + id
              + '">&nbsp;</div>';
          that.infot = $('#' + id);
        }
        // fire ajax request for rich content
        $.ajax({
          url : '/legacy/node/' + nid + '/sub/' + sid,
          success : function(data) {
            if (false && console && console.log) {
              console.log('Sample of data:', data.slice(0, 100));
            }
            // write data to info target
            that.infot.html('<div class="inuse">' + data + '</div>');
          }
        });
        // remove last selected marker if set
        if (that.marker) {
          that.marker.setMap(null);
        }
        // tweak event's coords to make them work as marker inputs
        kmlEvent.latLng.Ra += 0.0;
        // show a 'selected' marker
        that.marker = new that.gmaps.Marker({
          position: kmlEvent.latLng,
          map: that.map,
          title:"selected"
        });
      };
    },

    /**
     * @param object that Context from caller (this)
     * @return function Listener for handling map zoom events
     */
    kmlZoomEvent : function(that) {
      return function() {
        var turningPoint = 8, oldlvl = that.zoomLevel;
        // update zoom level
        that.zoomLevel = that.map.getZoom();
        // catch zoom in
        if (oldlvl <= turningPoint && that.zoomLevel > turningPoint) {
          // if (console && console.log) console.log('zooming in past turning point - detach');
          // that.kmlLayer.setMap(null);
        }
        // catch zoom out
        if (oldlvl > turningPoint && that.zoomLevel <= turningPoint) {
          // if (console && console.log) console.log('zooming out past turning point - attach');
          // that.kmlLayer.setMap(that.map);
        }
      };
    },

    
    /**
     * @param {number=}
     * Component ID
     * @param {number=}
     * Sub-component ID
     * @param {number=}
     * Comparison method
     * @return string Path to KML
     */
    kmlGetPath : function() {
      var cid = null, scid = null, compm = null, pathadd = null, path;
      // dereference optional arguments
      if (arguments > 0) {
        cid = arguments[0];
      }
      if (arguments > 1) {
        scid = arguments[1];
      }
      if (arguments > 2) {
        compm = arguments[2];
      }
      // build path to return
      pathadd = (cid != null ? '&cid=' + cid : '')
          + (scid != null ? '&scid=' + scid : '')
          + (compm != null ? '&compm=' + compm : '');
      path = this.kmlPath + pathadd;
      return path;
    }
  };
})(jQuery);

$(document).ready(function() {
  var canvas = document.getElementById("map_canvas");
  if (canvas) {
    // create a map of the UK if there's a #map_canvas on the page
    var latlng = new google.maps.LatLng(53.821081, -3.995078);
    var mapOptions = {
      zoom : 6,
      center : latlng,
      streetViewControl : false,
      mapTypeControl : false,
      mapTypeId : google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(canvas, mapOptions);

    gmapmark.init(map, google.maps);
    // trigger map resize
    gmapmark.resize();
  }
});
;
