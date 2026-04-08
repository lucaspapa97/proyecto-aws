import json

def lambda_handler(event, context):
    # Mensaje de respuesta
    mensaje = "Hola Mundo desde AWS Lambda"
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': mensaje,
            'input_event': event
        })
    }
