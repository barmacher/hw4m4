from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ActiveTagSerializer, CreateProductValidateSerializer


@api_view(['GET','POST'])
def products_list_view(request):
    if request.method == 'POST':
        serializer = CreateProductValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data={"message":'ERROR!',
                      'errors': serializer.errors}

            )
        title = request.data.get('title', '')
        discription = request.data.get('discription','')
        price = request.data.get('price',0)
        products = Product.objects.create(title=title,discription=discription,price=price)
        products.category.set(request.data['category'])
        products.save()
        return Response(data={'message': 'you created product',
                              'products': ProductSerializer(products).data})

    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)





@api_view(['GET','PUT','DELETE'])
def products_item_views(request,pk):
    try:
        products = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(data={'message': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        products.delete()
        return Response(data={'message': 'Продукт удалён!'})
    elif request.method == 'PUT':
        products.title - request.data.get('title')
        products.discriptiob - request.data.get('discription')
        products.price - request.data.get('price')
        products.category - request.data.get('category')
        products.tags(request.data.get('tags'))
        products.save()
        return Response(data={'message': 'Product updated',
                              'movie': ProductSerializer(products).data})
    data = ProductSerializer(products, many=False).data
    return Response(data=data)


# @api_view(['GET'])
# def products_item_views(request,pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         return Response(data={'message': 'Product not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     data = ProductSerializer(product, many=False).data
#     return Response(data=data)

@api_view(['GET'])
def tags_views(request):
    products = Product.objects.all()
    data = ActiveTagSerializer(products, many=True).data
    return Response(data=data)

