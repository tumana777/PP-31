# from django.utils.deprecation import MiddlewareMixin
#
# class RequestTimeMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         print("This is a middleware from request")
#
#     def process_response(self, request, response):
#         print("This is a middleware from response")
#         return response

import time

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        t1 = time.time()

        response = self.get_response(request)

        t2 = time.time()

        total = t2 - t1

        print(f"Request: {request.method},Path: {request.path}, user: {request.user}, IP:{request.META['REMOTE_ADDR']}, took: {total:.3f} seconds")

        return response