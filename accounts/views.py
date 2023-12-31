from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

import string, random

from accounts.models import User

# Create your views here.
# 회원가입
@api_view(['POST'])
@permission_classes([AllowAny])
def signup_view(request):
    user_name = request.data['user_name']
    user_id = request.data['user_id']
    phone_number = request.data['phone_number']
    password = request.data['password']

    # 아이디 중복 확인
    if User.objects.filter(user_id=user_id).exists():
        return Response({'message': '이미 가입된 아이디입니다.'}, status=405)

    user = User.objects.create_user(
        user_name=user_name,
        user_id=user_id,
        phone_number=phone_number,
        password=password
    )

    user.save()

    return Response(status=200)


# 로그인
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    user_id = request.data['user_id']
    password = request.data['password']

    user = authenticate(request, user_id=user_id, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})
    else:
        return Response({'message': '비밀번호를 잘못 입력했습니다.'}, status=401)
    

# 로그인 만료 확인
@api_view(['GET'])
def check_view(request):
    return Response(status=200)


# 아이디 찾기
@api_view(['POST'])
@permission_classes([AllowAny])
def search_id_view(request):
    user_name = request.data['user_name']
    phone_number = request.data['phone_number']

    if not User.objects.filter(user_name=user_name, phone_number=phone_number).exists():
        return Response({'message': '해당 사용자 정보가 없습니다.'}, status=404)
    
    user = User.objects.get(user_name=user_name, phone_number=phone_number)

    return Response({'user_id': user.user_id}, status=200)


# 비밀번호 찾기
@api_view(['POST'])
@permission_classes([AllowAny])
def search_password_view(request):
    user_name = request.data['user_name']
    user_id = request.data['user_id']
    phone_number = request.data['phone_number']

    if not User.objects.filter(
        user_name=user_name,
        user_id=user_id,
        phone_number=phone_number
    ).exists():
        return Response({'message': '해당 사용자 정보가 없습니다.'}, status=404)
    
    user = User.objects.get(user_name=user_name, user_id=user_id, phone_number=phone_number)
    tmp_password = ''.join(random.sample(string.ascii_letters, 30))
    user.set_password(tmp_password)
    user.save()

    return Response({'password': tmp_password}, status=200)


# 비밀번호 확인
@api_view(['POST'])
def verify_view(request):
    password = request.data['password']

    user = authenticate(request, user_id=request.user, password=password)

    if user:
        return Response(status=200)
    else:
        return Response({'message' : '비밀번호를 잘못 입력했습니다.'}, status=400)


# 비밀번호 수정
@api_view(['PUT'])
def modify_password_view(request):
    password = request.data['password']

    user = User.objects.get(id=request.user.id)
    user.set_password(password)
    user.save()

    return Response(status=200)


# 회원정보 수정
@api_view(['PUT'])
def modify_personal_information_view(request):
    user_name = request.data['user_name']
    phone_number = request.data['phone_number']

    user = User.objects.get(id=request.user.id)

    user.user_name = user_name
    user.phone_number = phone_number

    user.save()

    return Response(status=200)


# 회원 탈퇴
@api_view(['DELETE'])
def withdraw_view(request):
    password = request.data['password']

    user = authenticate(request, user_id=request.user, password=password)

    if user:
        user.delete()
        return Response(status=200)
    else:
        return Response({'message': '비밀번호를 잘못 입력했습니다.'}, status=400)