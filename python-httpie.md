# Python HTTPie

### Installation

    pip install --upgrade httpie

### GET/POST/PUT/DELETE examples

    http GET localhost:8000/items
    http POST localhost:8000/items first_name="jeremy"
    http PUT localhost:8000/items/fbc5355c-2f0c-42a6-abdb-b28bb812496e first_name="jeremy2"
    http DELETE localhost:8000/items/fbc5355c-2f0c-42a6-abdb-b28bb812496e

