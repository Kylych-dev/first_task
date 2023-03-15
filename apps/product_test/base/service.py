from django.core.exceptions import ValidationError

def get_path_upload_image(instance, file):
    ''' format: (media)/avatar/user_id/photo.jpg'''
    return f'avatar/{instance.id}/{file}'

def validate_size_image(file_obj):
    '''check file size'''
    megabyte_limit = 2 
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f'maximum size file {megabyte_limit}MB')