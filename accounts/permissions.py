from rest_framework import permissions

class IsUserOrReadonly(permissions.BasePermission):
	# 인증된 유저에 한해, 목록조회/포스팅등록을 허용
	def has_permission(self, request, view):
		return request.user.is_authenticated

	# 작성자에 한해, Record에 대한 수정/삭제 허용
	def has_object_permission(self, request, view, obj):
		# 조회 요청(GET, HEAD, OPTIONS) 에 대해서는 인증여부에 상관없이 허용
		if request.method in permissions.SAFE_METHODS:
			return True

		# PUT, DELETE 요청에 대해, 작성자일 경우에만 요청 허용
		return obj.email == request.user.email

class IsUserOnly(permissions.BasePermission):
	# 인증된 유저에 한해, 목록조회/포스팅등록을 허용
	def has_permission(self, request, view):
		return request.user.is_authenticated

	# 본인에 한해, Record에 대한 조회/수정/삭제 허용
	def has_object_permission(self, request, view, obj):

		# 조회 요청의 경우, 본인에게만 허용
		if (request.method == 'GET'):
			return obj.email == request.user.email

		# PUT, DELETE 요청에 대해, 본인일 경우에만 요청 허용
		return obj.email == request.user.email


class IsUserUpdateOrReadonly(permissions.BasePermission):
	# 인증된 유저에 한해, 목록조회/포스팅등록을 허용
	def has_permission(self, request, view):
		return request.user.is_authenticated

	# superuser에게는 삭제 권한만 부여하고
	# 작성자에게는 수정 권한만 부여
	def has_object_permission(self, request, view, obj):
		# 조회 요청(GET, HEAD, OPTIONS) 에 대해서는 인증여부에 상관없이 허용
		if request.method in permissions.SAFE_METHODS:
			return True

		# 삭제 요청의 경우, superuser에게만 허용
		if (request.method == 'DELETE'):
			return request.user.is_superuser

		# PUT 요청에 대해, 작성자일 경우에만 요청 허용
		return obj.email == request.user.email