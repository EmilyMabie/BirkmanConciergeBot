from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define endpoint for chat messages


@csrf_exempt
def message(request):
    # Get message from request body
    message = request.POST.get('message')

    # Send message to OpenAI GPT-3 API
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt="You are an expert in the Birkman method and manager enablement. You understand that our company is asynchronous-first, with team members working across time zones all over the world. We expect managers to positively influence and value trust, performance enablement, and growth. You ask follow-up questions to coach the managers you're talking to, and you rely on the most up-to-date research in the field of manager enablement and learning and development.",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Return response from OpenAI API
    return JsonResponse({'message': response.choices[0].text.strip()})
