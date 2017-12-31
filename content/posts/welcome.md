title: Welcome to my site
slug: welcome
category: posts
date: 2017-12-31
modified: 2017-12-31

I have been procrastinating for a long time about putting together an updated personal website, in the hopes of getting into a more regular writing routine. This winter break has finally afforded me the time to get off butt and do it.

A perennial struggle of mine when it comes to starting a new project is paralysis around choosing a new framework or direction. "Don't overthink it" is something that I find I have to remind myself constantly about. At the end of the day, it's always better to make a choice, even if it's the wrong one, and produce something rather than spending countless hours reading through articles and debates. 

I'll write about my setup in more detail in a future post, especially since this site is very much a work-in-progress, but after much internal debate I've decided to keep things relatively simple. I had considered using this opportunity to gain more experience playing with containers and kubernetes but quickly realized that 99% of what I wanted out of this site was ultimately static-content. And since I don't expect a ton of traffic anytime soon I don't need to be paying for all that idle CPU time.

I've come to love [Bear](http://www.bear-writer.com/), and I knew I wanted to write my content in markdown, so I narrowed my search to static site generators that supported markdown. Very quickly I settled on [Pelican](https://getpelican.com/), as it seemed in relatively active development and checked of a lot of boxes for me.

Regarding hosting, I'm publishing the site to an S3 bucket and using CloudFront to make everything speedy (and handle TLS). It had been a while since I launched anything on AWS, and am still amazed how quickly I cut over everything to the new site from my old hosting. I did go down a bit of a rabbit hole on [favicons](https://realfavicongenerator.net/blog/favicon-why-youre-doing-it-wrong/), but I feel good about this starting point.

If you're visiting this site on a mobile device, I know the theme I have configured is not responsive, and it's one of the first things I hope to address. I spend most of my time on backend development, so it's a good excuse for me to update my frontend skills.

I'm also a relatively new father, so I may detour into posts on things that I've learned while raising my daughter through her first year of life and beyond. 