# REST

### RESTful methods

Against collection resources (e.g. /items/):

    POST: Create new instance in the collection (not idempotent)
    PUT: Replace the entire collection (idempotent)
    GET: List the URI's inside the collection, and possibly members
    DELETE: Delete the entire collection

Against a member/element (e.g. /items/1):

    PUT: Replace (update) the specified member
    GET: Retrieve member
    DELETE: Delete the member
    
