(function(){var f=this;var k=function(a,b){for(var e in a)Object.prototype.hasOwnProperty.call(a,e)&&b.call(null,a[e],e,a)};var l,m,n,p,q=function(){return f.navigator?f.navigator.userAgent:null};p=n=m=l=!1;var s;if(s=q()){var t=f.navigator;l=0==s.lastIndexOf("Opera",0);m=!l&&(-1!=s.indexOf("MSIE")||-1!=s.indexOf("Trident"));n=!l&&-1!=s.indexOf("WebKit");p=!l&&!n&&!m&&"Gecko"==t.product}var u=m,w=p,x=n;var z;if(l&&f.opera){var A=f.opera.version;"function"==typeof A&&A()}else w?z=/rv\:([^\);]+)(\)|;)/:u?z=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/:x&&(z=/WebKit\/(\S+)/),z&&z.exec(q());var B=function(a){this.b=[];this.a={};for(var b=0,e=arguments.length;b<e;++b)this.a[arguments[b]]=""};B.prototype.c=function(a){return this.a.hasOwnProperty(a)?this.a[a]:""};B.prototype.geil=B.prototype.c;var D=function(){var a=C,b=[];k(a.a,function(a){""!=a&&b.push(a)});return 0<a.b.length&&0<b.length?a.b.join(",")+","+b.join(","):a.b.join(",")+b.join(",")};var C,E="google_conversion_id google_conversion_format google_conversion_type google_conversion_order_id google_conversion_language google_conversion_value google_conversion_currency_code google_conversion_domain google_conversion_label google_conversion_color google_disable_viewthrough google_remarketing_only google_remarketing_for_search google_conversion_items google_custom_params google_conversion_date google_conversion_time google_conversion_js_version onload_callback opt_image_generator google_is_call google_conversion_page_url".split(" ");
function F(a){return null!=a?escape(a.toString()):""}function H(a,b){var e=F(b);if(""!=e){var c=F(a);if(""!=c)return"&".concat(c,"=",e)}return""}function I(a){var b=typeof a;return null==a||"object"==b||"function"==b?null:String(a).replace(/,/g,"\\,").replace(/;/g,"\\;").replace(/=/g,"\\=")}
function J(a){var b;if((a=a.google_custom_params)&&"object"==typeof a&&"function"!=typeof a.join){var e=[];for(b in a)if(Object.prototype.hasOwnProperty.call(a,b)){var c=a[b];if(c&&"function"==typeof c.join){for(var d=[],g=0;g<c.length;++g){var h=I(c[g]);null!=h&&d.push(h)}c=0==d.length?null:d.join(",")}else c=I(c);(d=I(b))&&null!=c&&e.push(d+"="+c)}b=e.join(";")}else b="";return""==b?"":"&".concat("data=",encodeURIComponent(b))}
function K(a){return"number"!=typeof a&&"string"!=typeof a?"":F(a.toString())}function L(a){if(!a)return"";a=a.google_conversion_items;if(!a)return"";for(var b=[],e=0,c=a.length;e<c;e++){var d=a[e],g=[];d&&(g.push(K(d.value)),g.push(K(d.quantity)),g.push(K(d.item_id)),g.push(K(d.adwords_grouping)),g.push(K(d.sku)),b.push("("+g.join("*")+")"))}return 0<b.length?"&item="+b.join(""):""}
function M(a,b,e){var c=[];if(a){var d=a.screen;d&&(c.push(H("u_h",d.height)),c.push(H("u_w",d.width)),c.push(H("u_ah",d.availHeight)),c.push(H("u_aw",d.availWidth)),c.push(H("u_cd",d.colorDepth)));a.history&&c.push(H("u_his",a.history.length))}e&&"function"==typeof e.getTimezoneOffset&&c.push(H("u_tz",-e.getTimezoneOffset()));b&&("function"==typeof b.javaEnabled&&c.push(H("u_java",b.javaEnabled())),b.plugins&&c.push(H("u_nplug",b.plugins.length)),b.mimeTypes&&c.push(H("u_nmime",b.mimeTypes.length)));
return c.join("")}function N(a,b,e){var c="";if(b){var c=c+H("ref",null!=b.referrer?b.referrer.toString().substring(0,256):""),d;if(a.top==a)d=0;else if(b=a.location.ancestorOrigins)d=b[b.length-1]==a.location.origin?1:2;else{b=a.top;try{d=!!b.location.href||""===b.location.href}catch(g){d=!1}d=d?1:2}b="";b=e?e:1==d?a.top.location.href:a.location.href;c+=H("url",null!=b?b.toString().substring(0,256):"");c+=H("frm",d)}return c}
function O(a){return a&&a.location&&a.location.protocol&&"https:"==a.location.protocol.toString().toLowerCase()?"https:":"http:"}function P(){return new Image}function Q(a,b,e){var c=P;"function"===typeof a.opt_image_generator&&(c=a.opt_image_generator);c=c();b+=H("async","1");c.src=b;c.onload=e&&"function"===typeof a.onload_callback?a.onload_callback:function(){}}
function R(a){for(var b=window,e={},c=function(c){e[c]=a&&null!=a[c]?a[c]:b[c]},d=0;d<E.length;d++)c(E[d]);c("onload_callback");return e};window.google_trackConversion=function(a){a=R(a);a.google_conversion_format=3;var b;var e=window,c=navigator,d=document,g=!1;if(a&&3==a.google_conversion_format){try{var h;"landing"==a.google_conversion_type||!a.google_conversion_id||a.google_remarketing_only&&a.google_disable_viewthrough?h=!1:(a.google_conversion_date=new Date,a.google_conversion_time=a.google_conversion_date.getTime(),a.google_conversion_snippets="number"==typeof a.google_conversion_snippets&&0<a.google_conversion_snippets?a.google_conversion_snippets+
1:1,"number"!=typeof a.google_conversion_first_time&&(a.google_conversion_first_time=a.google_conversion_time),a.google_conversion_js_version="7",0!=a.google_conversion_format&&1!=a.google_conversion_format&&2!=a.google_conversion_format&&3!=a.google_conversion_format&&(a.google_conversion_format=1),C=new B(1),h=!0);if(h){h="/?";"landing"==a.google_conversion_type&&(h="/extclk?");var S=O(e)+"//"+(a.google_remarketing_only?"googleads.g.doubleclick.net":a.google_conversion_domain||"www.googleadservices.com")+
"/pagead/"+[a.google_remarketing_only?"viewthroughconversion/":"conversion/",F(a.google_conversion_id),h,"random=",F(a.google_conversion_time)].join(""),v;n:{var G=a.google_conversion_language;if(null!=G){var r=G.toString();if(2==r.length){v=H("hl",r);break n}if(5==r.length){v=H("hl",r.substring(0,2))+H("gl",r.substring(3,5));break n}}v=""}b=[H("cv",a.google_conversion_js_version),H("fst",a.google_conversion_first_time),H("num",a.google_conversion_snippets),H("fmt",a.google_conversion_format),H("value",
a.google_conversion_value),H("currency_code",a.google_conversion_currency_code),H("label",a.google_conversion_label),H("oid",a.google_conversion_order_id),H("bg",a.google_conversion_color),v,H("guid","ON"),H("disvt",a.google_disable_viewthrough),H("is_call",a.google_is_call),L(a),M(e,c,a.google_conversion_date),N(e,d,a.google_conversion_page_url),J(a),a.google_remarketing_for_search&&!a.google_conversion_domain?"&srr=n":"",H("eid",D())].join("");Q(a,S+b,!0);if(a.google_remarketing_for_search&&!a.google_conversion_domain){var y=
O(e)+"//www.google.com/ads/user-lists/"+[F(a.google_conversion_id),"/?random=",Math.floor(1E9*Math.random())].join(""),y=y+[H("label",a.google_conversion_label),H("fmt","3"),N(e,d,a.google_conversion_page_url)].join("");Q(a,y,!1)}g=!0}}catch(T){}b=g}else b=!1;return b};})();
