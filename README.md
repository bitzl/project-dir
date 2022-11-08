# Static site to work with digital art

## Basic Content Structure

```
PROJECT: A collection of generated art that is somehow related
     |
  contains multiple
     |
ITEMS: Pieces of art that each can consist of one or more images that should be viewed together - e.g. several stages during the generation process. Each item has a IIIF manifest containing these images.
     |
  contains multiple
     |
IMAGES: The final images, available via IIIF.
```


## Deployment Ideas

### Git + CI

In this scenario, publishing would mean to generate the project content files to the Git repository, commit and push them. Then the CI would build the site and publish it to the web server.

### Running Hugo locally on the server

This would mean to have a checked out verison of the repository on the server and have the publishing scripts copy the content files into Hugo's content directory. Then the site would be built and published by running Hugo on the server.
