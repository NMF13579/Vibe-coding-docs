/**
 * Theme (window.name), hash routing, install tabs, copy buttons, Lucide icons.
 * No localStorage — works in iframe contexts.
 */
(function () {
  "use strict";

  var STATE_KEY = "vibeDocsUi";

  function parseState() {
    try {
      var raw = window.name;
      if (!raw) return {};
      var o = JSON.parse(raw);
      return o && typeof o === "object" ? o : {};
    } catch (e) {
      return {};
    }
  }

  function saveState(partial) {
    var next = Object.assign({}, parseState(), partial);
    next._k = STATE_KEY;
    window.name = JSON.stringify(next);
  }

  function getTheme() {
    var s = parseState();
    return s.theme === "dark" ? "dark" : "light";
  }

  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    saveState({ theme: theme });
    updateThemeToggle(theme);
  }

  function updateThemeToggle(theme) {
    var sun = document.querySelector("[data-theme-icon='sun']");
    var moon = document.querySelector("[data-theme-icon='moon']");
    if (!sun || !moon) return;
    var isDark = theme === "dark";
    sun.style.display = isDark ? "none" : "block";
    moon.style.display = isDark ? "block" : "none";
    var btn = document.getElementById("theme-toggle");
    if (btn) btn.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
  }

  function normalizeHash(hash) {
    if (!hash || hash === "#") return "#home";
    return hash.split("?")[0];
  }

  function getRoute() {
    return normalizeHash(window.location.hash || "#home");
  }

  function showView(route) {
    var views = document.querySelectorAll(".view");
    var i;
    for (i = 0; i < views.length; i++) {
      views[i].classList.remove("is-active");
      views[i].hidden = true;
    }
    var id = route === "#home" ? "view-home" : "view-" + route.slice(1);
    var el = document.getElementById(id);
    if (el) {
      el.hidden = false;
      el.classList.add("is-active");
    } else {
      var home = document.getElementById("view-home");
      if (home) {
        home.hidden = false;
        home.classList.add("is-active");
      }
    }
    if (typeof lucide !== "undefined" && lucide.createIcons) {
      lucide.createIcons();
    }
  }

  function onHashChange() {
    showView(getRoute());
    window.scrollTo(0, 0);
  }

  function bindRoleCards() {
    var cards = document.querySelectorAll("[data-role-hash]");
    var j;
    for (j = 0; j < cards.length; j++) {
      cards[j].addEventListener("click", function () {
        var h = this.getAttribute("data-role-hash");
        if (h) window.location.hash = h;
      });
    }
  }

  function bindBackButtons() {
    var backs = document.querySelectorAll("[data-back-home]");
    var k;
    for (k = 0; k < backs.length; k++) {
      backs[k].addEventListener("click", function () {
        window.location.hash = "#home";
      });
    }
  }

  function bindInstallTabs() {
    var tablist = document.querySelector("[role='tablist']");
    if (!tablist) return;

    var tabs = tablist.querySelectorAll("[role='tab']");
    var panels = document.querySelectorAll(".tab-panel");

    function activateTab(selected) {
      var t;
      for (t = 0; t < tabs.length; t++) {
        var tab = tabs[t];
        var sel = tab === selected;
        tab.setAttribute("aria-selected", sel ? "true" : "false");
        tab.tabIndex = sel ? 0 : -1;
      }
      var panelId = selected.getAttribute("aria-controls");
      var p;
      for (p = 0; p < panels.length; p++) {
        panels[p].classList.remove("is-active");
        panels[p].hidden = true;
      }
      var panel = document.getElementById(panelId);
      if (panel) {
        panel.hidden = false;
        panel.classList.add("is-active");
      }
    }

    var n;
    for (n = 0; n < tabs.length; n++) {
      (function (tab) {
        tab.addEventListener("click", function () {
          activateTab(tab);
        });
        tab.addEventListener("keydown", function (e) {
          var keys = ["ArrowLeft", "ArrowRight", "Home", "End"];
          if (keys.indexOf(e.key) === -1) return;
          e.preventDefault();
          var idx = Array.prototype.indexOf.call(tabs, tab);
          var next = idx;
          if (e.key === "ArrowRight") next = (idx + 1) % tabs.length;
          else if (e.key === "ArrowLeft") next = (idx - 1 + tabs.length) % tabs.length;
          else if (e.key === "Home") next = 0;
          else if (e.key === "End") next = tabs.length - 1;
          tabs[next].focus();
          activateTab(tabs[next]);
        });
      })(tabs[n]);
    }

    var first = tabs[0];
    if (first) activateTab(first);
  }

  function bindCopyButtons() {
    document.body.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-copy-target]");
      if (!btn) return;
      var id = btn.getAttribute("data-copy-target");
      var pre = document.getElementById(id);
      if (!pre) return;
      var text = pre.textContent || "";
      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.left = "-9999px";
        document.body.appendChild(ta);
        ta.select();
        try {
          document.execCommand("copy");
        } catch (err) {}
        document.body.removeChild(ta);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).catch(fallback);
      } else {
        fallback();
      }
      var orig = btn.getAttribute("aria-label") || "Copy";
      btn.setAttribute("aria-label", "Copied");
      setTimeout(function () {
        btn.setAttribute("aria-label", orig);
      }, 2000);
    });
  }

  function bindThemeToggle() {
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme") || "light";
      setTheme(cur === "dark" ? "light" : "dark");
    });
  }

  function initIcons() {
    if (typeof lucide !== "undefined" && lucide.createIcons) {
      lucide.createIcons();
    }
  }

  function init() {
    var theme = getTheme();
    document.documentElement.setAttribute("data-theme", theme);
    updateThemeToggle(theme);

    bindThemeToggle();
    bindRoleCards();
    bindBackButtons();
    bindInstallTabs();
    bindCopyButtons();

    window.addEventListener("hashchange", onHashChange);
    if (!window.location.hash || window.location.hash === "#") {
      window.location.replace(window.location.pathname + window.location.search + "#home");
    } else {
      onHashChange();
    }

    initIcons();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
