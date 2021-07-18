import logging
import azure.functions as func


def main(req: func.HttpRequest, outputblob: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    result = req.get_json()
    result['param'] = name

    outputblob.set(str(result))

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "Pass a name in the query string or in the request body.",
             status_code=400
        )
