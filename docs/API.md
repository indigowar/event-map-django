# API

## Organizer_level

To retrieve a list of organizers levels use: `GET` to `api/v1/organizer_level`

### Response

```json
[
  {
    "id": 1,
    "name": "name a",
    "code": "COD"
  },
  {
    "id": 1,
    "name": "name a",
    "code": "COD"
  },
  {
    "id": 1,
    "name": "name a",
    "code": "COD"
  },
  {
    "id": 1,
    "name": "name a",
    "code": "COD"
  }
]
```

## Organizer

### Retrieve a list

Retrieve a list of organizers use `GET` to `api/v1/organizer`

#### Response

```json
[
  {
    "id": 1,
    "name": "name a",
    "logo": "logo",
    "level": 1
  },
  {
    "id": 1,
    "name": "name a",
    "logo": "logo",
    "level": 1
  },
  {
    "id": 1,
    "name": "name a",
    "logo": "logo",
    "level": 1
  }
]
```

### Create new organizer

Create a new organizer using `POST` to `api/v1/organizer`

#### Request

```json
{
  "name": "name ",
  "logo": "looogooo",
  "code": 5
}
```

#### Response

```json
{
  "id": 12312313,
  "name": "name ",
  "logo": "looogooo",
  "code": 5
}
```

### Retrieve one organizer

To retrieve organizer use `GET` to `api/v1/organizer/{id}`, where `id` is id the id of organizer.

#### Response

```json
{
  "id": 12312313,
  "name": "name ",
  "logo": "looogooo",
  "code": 5
}
```

### Delete organizer

To delete an organizer use `DELETE` to `api/v1/organizer/{id}`, where `id` is the id of organizer.

### Update organizer

Update organizer using `PUT` to `api/v1/organizer/{id}` where `id` is id of organizer.

#### Request

```json
{
  "id": 1,
  "name": "name ",
  "logo": "looogooo",
  "code": 5
}
```

#### Response

```json
{
  "id": 12312313,
  "name": "name ",
  "logo": "looogooo",
  "code": 5
}
```

## Competitor

To retrieve all competitors use `GET` to `api/v1/competitor/{id}`:

### Filtration

The base API route is `api/v1/event/?`.

To filtrate by something you need add to this path next arguments, separated in a path by `&`:

| PATH                                        | ARGUMENT                                | What filtering                           |
|---------------------------------------------|-----------------------------------------|------------------------------------------|
| `id=1&id=2&id=100`                          | 1, 2, 100 - is ids of events            | filtrate by event id                     |
| `organizer_level=1&organizer_level=2`       | 1, 2 (ids of organizer levels)          | filtrate by this organizer levels        |
| `competitors=1&competitors=2&competitors=3` | 1, 2, 3(ids of competitors)             | filtrate by competitors of event         |
| `organizer=2&organizer=55`                  | 2, 55 - organizer's ids                 | filtrate by specific organizers          |
| `f_range_min=2`                             | 2 - is minimum of founding range        | filtate by minimum of founding range     |
| `f_range_max=100`                           | 100 - is a maximum of founding range    | filtrate by maximum of founding range    |
| `cf_range_min=2`                            | 2 - is minimum of co-founding range     | filtate by minimum of co-founding range  |
| `cf_range_max=100`                          | 100 - is a maximum of co-founding range | filtrate by maximum of co-founding range |
| `founding=1&founding=5`                     | 1, 5 - is IDs of founding types         | filtrate by founding types               |
| `trl=5&tlr=3&tlr=9`                         | values of TRL                           | filtate by trl                           |

### Response

```json
[
  {
    "id": 1,
    "name": "name"
  },
  {
    "id": 1,
    "name": "name"
  },
  {
    "id": 1,
    "name": "name"
  },
  {
    "id": 1,
    "name": "name"
  }
]
```

## FoundingType

To retrieve all founding types use `GET` to `api/v1/founding_type`.

### Response

```json
[
  {
    "id": 1,
    "name": "name "
  },
  {
    "id": 1,
    "name": "name "
  },
  {
    "id": 1,
    "name": "name "
  },
  {
    "id": 1,
    "name": "name "
  },
  {
    "id": 1,
    "name": "name "
  }
]
```

## Event

### Retrieve all

To retrieve all events use `GET` to `api/v1/event/`

#### Response

```json
[
  {
    "id": 2,
    "founding_range": {
      "id": 3,
      "low": 10,
      "high": 2555
    },
    "co_founding_range": {
      "id": 3,
      "low": 44,
      "high": 45
    },
    "subjects": [
      "subject 36",
      "subject 37",
      "subject 38",
      "subject 6545"
    ],
    "title": "title of event",
    "submission_deadline": "2023-04-11",
    "consideration_period": "cons.period",
    "realisation_period": "real.period",
    "result": "result",
    "site": "site",
    "document": "doc",
    "internal_contacts": "IC",
    "trl": 6,
    "organizer": 1,
    "precursor": 1,
    "founding_type": [],
    "competitors": [
      1,
      2,
      3
    ]
  }
]
```

### Create a new one

To create a new event use `POST` to `api/v1/event`

#### Request

```json
{
  "founding_range": {
    "low": 0,
    "high": 500000
  },
  "co_founding_range": {
    "low": 15,
    "high": 50
  },
  "subjects": [
    1,
    2,
    3
  ],
  "title": "",
  "submission_deadline": "08-06-2022",
  "consideration_period": "",
  "realisation_period": "",
  "result": "",
  "site": "",
  "document": "",
  "internal_contacts": "",
  "trl": 5,
  "organizer": 1,
  "precursor": null,
  "founding_type": [],
  "competitors": []
}
```

#### Response

```json
{
  "id": 2,
  "founding_range": {
    "id": 3,
    "low": 10,
    "high": 2555
  },
  "co_founding_range": {
    "id": 3,
    "low": 44,
    "high": 45
  },
  "subjects": [
    "subject 36",
    "subject 37",
    "subject 38",
    "subject 6545"
  ],
  "title": "title of event",
  "submission_deadline": "2023-04-11",
  "consideration_period": "cons.period",
  "realisation_period": "real.period",
  "result": "result",
  "site": "site",
  "document": "doc",
  "internal_contacts": "IC",
  "trl": 6,
  "organizer": 1,
  "precursor": 1,
  "founding_type": [],
  "competitors": [
    1,
    2,
    3
  ]
}
```

### Retrieve one by id

To retrieve an event by it's use `GET` to `api/v1/event/{id}` where `id` is id of event.

#### Response

```json
{
  "id": 2,
  "founding_range": {
    "id": 3,
    "low": 10,
    "high": 2555
  },
  "co_founding_range": {
    "id": 3,
    "low": 44,
    "high": 45
  },
  "subjects": [
    "subject 36",
    "subject 37",
    "subject 38",
    "subject 6545"
  ],
  "title": "title of event",
  "submission_deadline": "2023-04-11",
  "consideration_period": "cons.period",
  "realisation_period": "real.period",
  "result": "result",
  "site": "site",
  "document": "doc",
  "internal_contacts": "IC",
  "trl": 6,
  "organizer": 1,
  "precursor": 1,
  "founding_type": [],
  "competitors": [
    1,
    2,
    3
  ]
}
```

### Update an event

To update a event `PUT` to `api/v1/event/{id}`

#### Request

```json
{
  "id": 1,
  "founding_range": {
    "id": 1,
    "low": 1,
    "high": 98
  },
  "co_founding_range": {
    "id": 1,
    "low": 0,
    "high": 0
  },
  "subjects": [
    "1111111111",
    "2222222222222222222",
    "3333333333333333",
    "44444444444444"
  ],
  "title": "aaaaaaaaaaaaaaaaaaaaaa",
  "submission_deadline": "2022-12-25",
  "consideration_period": "121111111111",
  "realisation_period": "111111111111111111",
  "result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
  "site": "111111111111111111111111111111111111111111111111111111",
  "document": "111111111111111111111111111111111111111111111111111111",
  "internal_contacts": "111111111111111111111111111111111111",
  "trl": 5,
  "organizer": 1,
  "precursor": null,
  "founding_type": [
    2
  ],
  "competitors": [
    1,
    2,
    3
  ]
}
```

#### Response

```json
{
  "id": 1,
  "founding_range": {
    "id": 1,
    "low": 1,
    "high": 98
  },
  "co_founding_range": {
    "id": 1,
    "low": 0,
    "high": 0
  },
  "subjects": [
    "1111111111",
    "2222222222222222222",
    "3333333333333333",
    "44444444444444"
  ],
  "title": "aaaaaaaaaaaaaaaaaaaaaa",
  "submission_deadline": "2022-12-25",
  "consideration_period": "121111111111",
  "realisation_period": "111111111111111111",
  "result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
  "site": "111111111111111111111111111111111111111111111111111111",
  "document": "111111111111111111111111111111111111111111111111111111",
  "internal_contacts": "111111111111111111111111111111111111",
  "trl": 5,
  "organizer": 1,
  "precursor": null,
  "founding_type": [
    2
  ],
  "competitors": [
    1,
    2,
    3
  ]
}
```

### Delete event

To delete an event use `DELETE` to `api/v1/event/{id}` where `id` is an id of event.