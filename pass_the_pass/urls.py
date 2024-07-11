from django.urls import path
from .views import SubmitData, CampingDetailView, CampingPatchView

urlpatterns = [
    path('submitData/', SubmitData.as_view(), name='submit_data'),
    path('detailData/<int:id>/', CampingDetailView.as_view(), name='camping_detail'),
    path('updateData/<int:pk>/', CampingPatchView.as_view(), name='camping_patch'),

]
