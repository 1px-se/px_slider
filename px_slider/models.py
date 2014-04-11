from cms.models import CMSPlugin
from filer.fields.folder import FilerFolderField

class SliderPlugin(CMSPlugin):
    album = FilerFolderField(verbose_name='Album')
    @property
    def images(self):
        if not hasattr(self, '__images'):
            files = self.album.files
            self.__images = [f for f in files if f.file_type == 'Image']
            self.__images.sort()
        return self.__images
