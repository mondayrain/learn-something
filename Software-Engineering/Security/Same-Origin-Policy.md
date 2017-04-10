# Same-origin Policy

**Same-origin policy** is an important concept in web app security.

Under this policy, a web browser permits scripts contained in web page A to access data in web page B _only if_ both web pages come from the same origin. An **origin** is defined as a combination of URI, hostname, and port number. This policy prevents a malicious script on one page from obtaining access to sensitive data on another web page through the the DOM.

The algorithm used to calculate the "origin" of a URI is specified in [RFC 6454](https://tools.ietf.org/html/rfc6454). In general, typical outcomes for checks against an URL will be positive if the compared URL has the same protocol (e.g. HTTP), host, and port. In other words, _the origin of a JS file is defined by the domain of the HTML page which includes it_.So for example, if you include Google Analytics code on your site with a <script> tag, it can do anything on your website but does not have the same origin permissions on the Google site.


#### Security Applications & Example

The Same-origin Policy helps protect sites that use authenticated sessions.

For example:

- A user is visiting a banking website and doesn't log out

- The user goes to another site that has some malicious JavaSCript code running in the background, which requests data from the banking site.

- Because the user is still logged into the banking site (and because of how the browser is complicit in maintaining sessions with the banking site's web server), the malicious code could do anything the user could do on the banking site.

The user visiting the malicious site would expect that the site should have no access to the banking session cookie. While it's true that the JavaScript has no _direct_ access to the cookie, it could still tell the browser to send/receive requests to the banking site using the cookie. _Because the script can do essentially the same thing a user would do_, even **[CSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery)** protection by the banking site would not be effective

When we use same-origin policy, the malicious site's JavaScript can't do anything with regard to Facebook, because the browser _won't let it_. Rather, it'll realize that e.g. malicious.js has an origin of http://malicious.com but is trying to run on http://bank.com/myaccount/dostuff... which has an origin of http://bank.com. Since the origins are different, malicious.js won't be allowed to run on the banking site.


#### Cross-origin Network Access

Same-origin policy controls interactions between 2 different origins, such as when you use `XMLHttpRequest` or an `<img>` element. These interactions are typically placed in 3 categories:

1. Cross-origin _writes_ are typically allowed (e.g. links, redirects, form submissions).

2. Cross-origin _embedding_ is typically allowed (e.g. JavaScript with <script src=>, CSS with links, <img> tags, fonts with @font-face, anything with frame and iframe).

3. Cross-origin _reads_ are typically **not** allowed. However, read access is often leaked by embedding...


#### Cross Site Scripting (XSS)

**Cross Site Scripting** or **XSS** is a vulnerability that allows an attacker inject JS code into a website, so that it originates from the attacked website _from the browser's  point of view_.

This can happen if the user input is not sufficiently sanitised. For example, a search function may display the string "Your search results for [userinput]". If [userinput] is not escaped/sanitised, an attacaker may search for:

```
<script>alert(document.cookie)</script>
```

The browser has no way to detect that this code was not provided by the website ownser, so it will execute it.

