from rest_framework import routers
from tips_promenad.views import QuizPointViewSet

router = routers.DefaultRouter()
router.register(r'users', QuizPointViewSet, base_name='users')

urlpatterns = router.urls

