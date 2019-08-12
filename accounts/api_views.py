from .serializers import *
from django.contrib.auth import get_user_model
from rest_framework import generics, parsers, renderers
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.views import APIView

from .permissions import IsUserOnly

class UserListView(generics.ListAPIView):
    """
        회원 리스트를 불러옵니다.

        ---
        # 권한
            - 관리자 권한이 있는 경우, 모든 유저 리스트를 불러옵니다.
            - 관리자 권한이 없는 경우, 해당 유저의 정보만 불러옵니다.

        # type
            - django, 카카오, 구글, 네이버로 분류됩니다.
            - django일 경우, 소셜 로그인이 아닌 오늘의 집에서 가입한 유저입니다.

        # 내용
            - id : 유저의 고유 ID
            - type : 소셜 로그인 분류
            - username : 닉네임
            - email : 이메일
            - social_profile : 소셜 로그인 프로필 이미지 URL
            - gender : 성별(1 = 남자, 2 = 여자)
            - birthday : 생년월일
            - message : 한줄 소개 내용
            - profile : 프로필 이미지
    """
    renderer_classes = [JSONRenderer] # JSON 형식으로만 받고 싶은 경우
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('email', 'username')

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(pk=self.request.user.id)
        return queryset

class UserCreateView(generics.CreateAPIView):
    """
        회원 계정을 생성합니다.

        ---
        다음과 같은 내용으로 요청할 수 있으며, 생성된 값이 리턴됩니다.

            - email : "사용할 이메일"
            - password : "사용할 비밀번호"
            - username : "사용할 닉네임"
    """
    serializer_class = UserCreateSerializer
    # 회원가입시 토근권한이 없어도 가입할 수 있도록 권한 부여
    permission_classes = (AllowAny,)

class UserUpdateView(generics.UpdateAPIView):
    """
        회원 리스트의 특정 id를 가지는 데이터를 수정합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        다음과 같은 내용으로 요청할 수 있으며, 수정된 값이 리턴됩니다.
        요청은 PUT, FETCH로 나뉩니다.
        profile의 경우, 파일을 업로드해야 하기 때문에 json으로 요청하실 수 없고 Postman을 사용해야 합니다.

        # 내용
            - username : "변경할 닉네임"
            - gender : 성별(1 = 남자, 2 = 여자)
            - birthday : "YYYY-MM-DD"
            - message : "변경할 한줄 소개 내용"
            - profile : "변경할 유저의 프로필 이미지(파일 업로드이므로 json으로 요청 불가)"
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserModifySerializer
    permission_classes = [IsUserOnly,]

class UserDetailView(generics.RetrieveAPIView):
    """
        회원 리스트의 특정 id를 가지는 데이터를 불러옵니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        # 내용
            - id : 유저의 고유 ID
            - username : 닉네임
            - email : 이메일
            - gender : 성별(1 = 남자, 2 = 여자)
            - birthday : 생년월일
            - message : 한줄 소개 내용
            - profile : 프로필 이미지
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsUserOnly,]

class UserDeleteView(generics.DestroyAPIView):
    """
        회원 리스트의 특정 id를 가지는 데이터를 삭제합니다.

        ---
        # 권한
            - 토큰 인증을 해야 합니다.

        회원 고유의 ID를 입력하면 삭제됩니다.
    """
    queryset = get_user_model().objects.all()
    permission_classes = [IsUserOnly,]

class UsernameObtainAuthToken(ObtainAuthToken):
    """
        회원의 Token key를 생성합니다.

        ---
        ### Swagger에서 현재 parameter 값이 출력되지 않습니다.
        ### Postman으로 다음과 같이 요청 테스트를 할 수 있습니다.
            1) Postman 주소에 "http://52.78.112.247/get_token/username/"을 입력하고 주소 왼쪽에 POST를 선택합니다.
            2) 주소 밑에 Body의 form-data를 선택합니다.
            3) KEY에 "username"과 "password"를 입력합니다.
            4) VALUE에 정보를 입력합니다.
            5) SEND를 누르고 Body의 내용을 확인합니다.

        ### 토큰을 사용하실 때에는 headers에 다음과 같이 입력합니다.
            1) 사용할 주소를 선택하고 headers를 선택합니다.
            2) KEY에 "Authorization"을 입력합니다.
            3) VALUE에 "Token 12313r3tw3wrgrgefqwrqwefw"을 입력하고 SEND를 누릅니다.(*****반드시 Token을 붙여야 합니다.)
            4) PUT, PATCH 요청인 경우, Body에 정보를 입력하고 SEND를 누릅니다.

        다음과 같은 내용으로 요청할 수 있습니다.

            - username : "회원가입된 유저 닉네임"
            - password : "회원가입된 유저 비밀번호"

        다음과 같은 내용으로 리턴됩니다.
        ex)
        ```
        {
            "token": "142wfawefrq23r23rqwdawdvw12db434"
        }
        ```
    """

# 오늘의 집 사이트에서 가입한 유저에게 발급하는 토큰 뷰
class EmailObtainAuthToken(APIView):
    """
        오늘의 집에서 가입한 회원의 Token key를 생성합니다.

        ---
        ### 소셜 로그인 사용자의 토큰은 "http://52.78.112.247/get_token/social/"로 요청하시기 바랍니다.
        ### Swagger에서 현재 parameter 값이 출력되지 않습니다.
        ### Postman으로 다음과 같이 요청 테스트를 할 수 있습니다.
            1) Postman 주소에 "http://52.78.112.247/get_token/"을 입력하고 주소 왼쪽에 POST를 선택합니다.
            2) 주소 밑에 Body의 form-data를 선택합니다.
            3) KEY에 "email"과 "password"를 입력합니다.
            4) VALUE에 정보를 입력합니다.
            5) SEND를 누르고 Body의 내용을 확인합니다.

        ### 토큰을 사용하실 때에는 headers에 다음과 같이 입력합니다.
            1) 사용할 주소를 선택하고 headers를 선택합니다.
            2) KEY에 "Authorization"을 입력합니다.
            3) VALUE에 "Token 12313r3tw3wrgrgefqwrqwefw"을 입력하고 SEND를 누릅니다.(*****반드시 Token을 붙여야 합니다.)
            4) PUT, PATCH 요청인 경우, Body에 정보를 입력하고 SEND를 누릅니다.

        다음과 같은 내용으로 요청할 수 있습니다.

            - email : "회원가입된 유저 이메일"
            - password : "회원가입된 유저 비밀번호"

        다음과 같은 내용으로 리턴됩니다.
        ex)
        ```
        {
            "token": "142wfawefrq23r23rqwdawdvw12db434"
        }
        ```
    """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

# 소셜 로그인으로 가입한 유저에게 발급하는 토큰 뷰
class SocialObtainAuthToken(APIView):
    """
            소셜 로그인 사용자의 Token key를 생성합니다.

            ---
            ### 오늘의 집 로그인을 통해 가입한 사용자의 토큰은 "http://52.78.112.247/get_token/"으로 요청하시기 바랍니다.
            ### Swagger에서 현재 parameter 값이 출력되지 않습니다.
            ### Postman으로 다음과 같이 요청 테스트를 할 수 있습니다.
                1) Postman 주소에 "http://52.78.112.247/get_token/social/"을 입력하고 주소 왼쪽에 POST를 선택합니다.
                2) 주소 밑에 Body의 form-data를 선택합니다.
                3) KEY에 "type", 'unique_user_id", "username", "email", "social_profile"을 입력합니다.
                4) VALUE에 정보를 입력합니다.
                5) SEND를 누르고 Body의 내용을 확인합니다.

            ### 토큰을 사용하실 때에는 headers에 다음과 같이 입력합니다.
                1) 사용할 주소를 선택하고 headers를 선택합니다.
                2) KEY에 "Authorization"을 입력합니다.
                3) VALUE에 "Token 12313r3tw3wrgrgefqwrqwefw"을 입력하고 SEND를 누릅니다.(*****반드시 Token을 붙여야 합니다.)
                4) PUT, PATCH 요청인 경우, Body에 정보를 입력하고 SEND를 누릅니다.

            다음과 같은 내용으로 요청할 수 있습니다.

                - type : "한글로 카카오, 구글, 네이버 3가지 중에 하나를 입력하세요."
                - unique_user_id : "소셜 로그인에서 받아온 정보 중에 UniqueID를 입력하세요."
                - username : "소셜 로그인에서 받아온 정보 중에 username을 입력하세요."
                - email : "소셜 로그인에서 받아온 정보 중에 email을 입력하세요."
                - social_profile : "소셜 로그인에서 받아온 정보 중에 profile image URL을 입력하세요."

            다음과 같은 내용으로 리턴됩니다.
            ex)
            ```
            {
                "token": "142wfawefrq23r23rqwdawdvw12db434"
            }
            ```
        """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = SocialAuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="type",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Type",
                        description="Valid Type for authentication",
                    ),
                ),
                coreapi.Field(
                    name="unique_user_id",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="UniqueID",
                        description="Valid UniqueID for authentication",
                    ),
                ),
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid Username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="Valid Email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="social_profile",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Social_profile",
                        description="Valid Social profile for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})