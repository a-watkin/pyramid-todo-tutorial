# Pyramid shell and config

You can use env variables, an ini or both for config.

To start the app:

`pserve config.ini`




The other argument, renderer, is optional but not really. If you don't specify a renderer, you have to deliberately construct the HTTP response you want to send back to the client using the Response object from pyramid.response. By specifying the renderer as a string, Pyramid knows to take whatever is returned by this function and wrap it in that same Response object with the MIME type of text/plain.


By default, Pyramid allows you to use string and json as renderers. If you've attached a templating engine to your application because you want to have Pyramid generate your HTML as well, you can point directly to your HTML template as your renderer.


You can't commit changes directly you have to use flush instead.