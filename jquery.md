# jQuery

### Include jQuery within HTML page

    ...
    <script src="http://code.jquery.com/jquery.min.js"></script>
    </body>
    </html>

### Ensure page has fully loaded before running scripts

    $(document).ready(function () {
        ...
    });
    
### Use jQuery object instead of $ alias

    $ == jQuery;
    
    // so 
    $(document) == jQuery(document);
    
### Post data using JSON content type

    $.ajax({
        url:url,
        type: "POST",
        data: JSON.stringify(object),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        ...
    })
