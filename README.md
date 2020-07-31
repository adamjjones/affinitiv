# Development Strategy

1. Open the PSD file and idenify all text, fonts and images.

2. View all the layers that make up the PSD file and export them as separate files.

3. Start coding a part of the PSD with HTML and CSS.

4. Make test accounts on different ESPs.

5. Complete one section and test on some ESPs on mobile devices and desktops.

6. Add the rest of the HTML and CSS and test periodically.

7. Add media queries.

8. Double check to ensure everything is done.

The email directory only has a python script that will send email to different service provider accounts.

In the public directory is a images directory and a index.html file. Those are the 2 items is where everything is. All the CSS is inline to increase performance because it was one less thing for the client to fetch.

There were also a couple places where I had to use tables for placement purposes because some email providers didn't support the postion CSS property.

Next Steps:

All placeholds would have to be templatized and have values from a database to take thoer place.
 
