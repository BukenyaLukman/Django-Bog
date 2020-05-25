from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.models import Profile
from blog.models import Post
from blog.api.serializers import PostSerializer

# @api_view(['GET',])
# def api_detail_blog_view(request, slug):
# 	try:
# 		blog_post = Post.objects.get(slug=slug)
# 	except Post.DoesNotexist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 		if request.method == "GET":
# 			serializer = PostSerializer(blog_post)
# 			return Response(serializer.data)

class PostAPIView(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
