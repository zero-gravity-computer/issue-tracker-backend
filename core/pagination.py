from base64 import b64decode, b64encode

def encode_cursor(obj):
    '''
    Given a model instance, encode its id and created_at
    properties into a string, called a "cursor".
    '''
    field_strings = [str(obj.id), str(obj.created_at)]
    payload = '|'.join(field_strings)
    payload_bytes = payload.encode('utf8')
    cursor_bytes = b64encode(payload_bytes)
    cursor = cursor_bytes.decode('utf8')
    return cursor


def decode_cursor(cursor):
    '''
    Given a cursor string, return the `id` and `created_at`
    that it encodes.
    '''
    cursor_bytes = cursor.encode('utf8')
    payload_bytes = b64decode(cursor_bytes)
    payload = payload_bytes.decode('utf8')
    field_strings = payload.split('|')
    return {
        "id": field_strings[0],
        "created_at": field_strings[1],
    }

def get_page(queryset, first, last, after=None, before=None):
    if first:
        if after is None:
            page = queryset.all()[:first]
            return page
        else:
            fields = decode_cursor(after)
            id = fields["id"]
            created_at = fields["created_at"]
            filtered_qs = queryset.filter(id__gt=id, created_at__gt=created_at)
            page = filtered_qs[:first]
            return page
    elif last:
        if before is None:
            page = queryset.all()[len(queryset)-last:]
            return page
        else:
            fields = decode_cursor(before)
            id = fields["id"]
            created_at = fields["created_at"]
            filtered_qs = queryset.filter(id__lt=id, created_at__lt=created_at)
            page = filtered_qs[len(filtered_qs)-last:]
            return page
    else:
        return queryset


#Testing Materials

'''
from core import models
c = models.Contributor.objects.all()
x = c[4]
cursor = encode_cursor(x)
page = get_page(c, 8)
print(page)
'''
