# burpomator

A small python wrapper to get started with automating BURP Professional scans via REST API.

## Usage

The BURP documentation can be found [here](https://portswigger.net/burp/documentation/desktop/settings/suite/rest-api).

1. Create and activate Python virtual environment
    
    ```sh
    python3 -m venv venv
    source ./venv/bin/activate
    ```

2. Install python packages

    ```sh
    pip install -r requirements.txt
    ```

3. Enable the REST API and create an API key in BURP

    ![Burpomator API Key](./static/gui.png)

4. Put the API key in your .env file (or use the `.env.example` file)

    ```sh
    echo API_KEY="<api_key>" > .env
    ```

5. Set your scan target or configure appropriate scan settings in `burpomator.py`

6. Run burpomator

    ```sh
    python3 burpomator.py
    ```

## Scan Configuration

A full scan configuration can be defined as follows:

```json
{
  "urls": [
    "<string>",
    "<string>"
  ],
  "name": "<string>",
  "scope": {
    "include": [
      {
        "rule": "<string>"
      },
      {
        "rule": "<string>"
      }
    ],
    "exclude": [
      {
        "rule": "<string>"
      },
      {
        "rule": "<string>"
      }
    ]
  },
  "application_logins": [
    {
      "username": "<string>",
      "password": "<string>"
    },
    {
      "username": "<string>",
      "password": "<string>"
    }
  ],
  "scan_configurations": [
    {
      "name": "<string>"
    },
    {
      "name": "<string>"
    }
  ],
  "resource_pool": "<string>",
  "scan_callback": {
    "url": "<string>"
  },
  "protocol_option": "httpAndHttps"
}
```

## Swagger

You can check out the API specs at:

`http://127.0.0.1:1337/<api_key>`

![BURP REST API](./static/restapi.png)

Also check out the `swagger.json` in `specs/burp_openapi.json` for the OpenAPI Specification file.
