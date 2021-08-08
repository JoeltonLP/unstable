class BaseSerializer:

    _model = None

    @classmethod
    def encode(cls, inst):
        
        data = {
            "pk": inst.pk,
            "name": inst.name,
            "email": inst.email,
            "phone": inst.phone
        }

        return data

    @classmethod
    def decode(cls, data):

        inst = cls._model(**data )

        return inst