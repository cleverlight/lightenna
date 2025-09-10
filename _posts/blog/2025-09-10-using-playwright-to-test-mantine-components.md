---
layout: single
title: Using Playwright to test Mantine components
description: Mantine is a popular React component library, but some aspects of testing it with Mantine can be tricky.
tags: tech coding
toc: true
header:
    overlay_image: /assets/images/techupdate_25318_1920x.jpg
    small_image: /assets/images/techupdate_25318_640x.jpg
---

## Select

* Mantine Select components are not HTML &lt;select&gt; elements, but a combination of &lt;input&gt; and &lt;div&gt; elements.
* To open the dropdown, click the input element.
* To select an option, click the &lt;div&gt; element that contains the option.

```javascript
await page.locator('[data-testid="SetStatusSelect"]').click();
await page.locator('div[value="archivePending"]').click();
await page.locator('[data-testid="SetStatusButton"]').click();
```

This code clicks the Mantine Menu to open it, selects the option with value "archivePending", and then clicks the button to submit the form.
I've used `data-testid` attributes to make the locators more robust, because they feature on a page with multiple similar components, which makes role-based isolation difficult.

Playwright's `selectOption` method does not work with Mantine Select components.
