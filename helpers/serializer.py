class BaseSerializer:

    _model = None

    @classmethod
    def encode(cls, inst):
        
        data = {
            'pk': inst.pk
        }

        return data

    @classmethod
    def decode(cls, data):
        inst = cls._model(**data )

        return inst