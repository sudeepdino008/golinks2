# Golinks2

I love the [golinks](https://github.com/GoLinks/golinks) project and thought that it's a decent project idea to implement while serving as a playground to learn django and other tech. The desired feature set is:
- ability to save links
- redirect to a link
- list the links and search through it - use webassembly and rust for the search feature
- have ability to specify the paths as aliases : `cs/papers/kafka` etc.
- list subdirectories (for example, when you do `go/ref`) 
- edit url 


This is meant to be a playground for trying new tech, so there'll be a lot of bells and whistles not necessary for the project, but the above fundamental aim should always work.

## More ideas:
- add logging framework
- containerize the application
- It can also be extended to have a personal toolkit - `t/` is the toolkit subdomain, wherein the subdomains open in an embedded webview. For example: `t/epoch` takes you to the eopchconverter website in an embedded view. Hence, a "toolkit"
- beautify the interface
- setup CI/CD (unit tests) only for the repo
- record search result performance (what rank search result is being selected?)
- use webassembly when introducing search
- performance tests


---
doubts:
- concurrency scenario in django - how are long running tasks handled? Does it block the further API use?
