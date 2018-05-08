requirejs.config({
  shim : {
    // 'jquery' : { 1.7.2 contains it's own shim },
    'jquery_transition' : {
      deps : [ 'jquery' ],
    },
    'jquery_ui' : {
      deps : [ 'jquery' ],
      exports : 'jQuery'
    },
    'jqu_touch_punch' : {
      deps : [ 'jquery_ui' ]
    },
    'banners_kb' : {
      deps : [ 'jquery' ]
    }
  },

  paths : {
    jquery : [ '//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min', '/misc/libs/jquery/1.7.2/jquery.min' ],
    jquery_transition : [ '/misc/libs/jquery/1.7.2/jquery.transition.min' ],
    jquery_ui : [ '//ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min', '/misc/libs/jqueryui/1.8.21/jquery-ui.min' ],
    jqu_touch_punch : [ '/misc/libs/jqueryui/1.8.21/jquery.ui.touch-punch.min' ],
    banners_kb_formatted : [ '../bckb/js/bckb-formatted' ],
    banners_kb : [ '../bckb/js/bannerscollection_kenburns' ]    
  }
});

// initialise the banner
// require([ 'jquery', 'jquery_transition', 'jquery_ui', 'jqu_touch_punch', 'banners_kb' ], function($){
require([ 'jquery', 'jquery_ui', 'jqu_touch_punch', 'banners_kb' ], function($){
  $('.bckb-inner').bannerscollection_kenburns({
    absUrl : '/sites/all/themes/frf/bckb/',
    skin : 'opportune',
    responsive : true,
    width100Proc : true,
    // note, bckb size is duplicated in view--featureslide.tpl.php
    width : 2048,
    height : 550,
    circleRadius : 12,
    circleLineWidth : 6,
    circleColor : "#ffffff", // 849ef3
    circleAlpha : 50,
    behindCircleColor : "#000000",
    behindCircleAlpha : 20,
    thumbsWrapperMarginTop : -80,
    showPreviewThumbs : false
  });
});
