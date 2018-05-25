import logging

class Typedefs:

    def __init__(self, json_file):
        self.json_file = json_file
        self.classification_defs = self._get_classification_defs()
        self.entity_defs = self._get_entity_defs()
        self.enum_defs = self._get_enum_defs()

    def _get_classification_defs(self):
        pass

    def _get_entity_defs(self):
        pass

    def _get_enum_defs(self):
        pass
    
    @property
    def typedefs_atlas_status(self):
        """ For each typedefs tells whether it is already in Atlas or not 

        Returns: 
           typedefs_status(dict): {typedef_name: <True,False>}
        """
        pass
    
    def create_in_atlas(types=None):
        """ Add typedefs if not exists already in Atlas

        types(list): any subset of ['classification', 'entity', 'enum']
        """
        try: 
            typedefs_to_load_in_atlas = {}
            if self.classification_defs is not None:
                logging.info('Adding classification defs')
                for classification in self.classification_defs:
                    if not self.typedefs_atlas_status()[classification['name']]:
                        typedefs_to_load_in_atlas.update(classification)

            if self.entity_defs is not None:
                logging.info('Adding entity defs')
                for entity in self.entity_defs:
                    if not self.typedefs_atlas_status()[entity['name']]:
                        typedefs_to_load_in_atlas.update(entity)
            
            if self.enum_defs is not None:
                logging.info('Adding enum defs')
                for entity in self.enum_defs:
                    if not self.typedefs_atlas_status()[enum['name']]:
                        typedefs_to_load_in_atlas.update(enum)
            call_create_typedefs(typedefs_to_load_in_atlas)

        except:
            pass
