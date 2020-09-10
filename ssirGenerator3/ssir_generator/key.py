import collections



#dict like attribute:{'widget':widget,'default':default}
#links name of attribute to widget,default value,list items


#site details
key=collections.OrderedDict()
key['site']={'widget':self.site,'default':''}
key['section']={'widget':self.section,'default':''}
key['start_ch']={'widget':self.start_ch,'default':0}
key['end_ch']={'widget':self.end_ch,'default':0}
key['section_length']={'widget':self.section_length,'default':0}
key['assesment_length']={'widget':self.assesment_length,'default':0}

#survey details
key['surveyor']={'widget':self.surveyor,'default':''}
key['survey_date']={'widget':self.survey_date,'default':QDate.currentDate().toString(widget_value.DATE_FORMAT)}
key['photo_ref']={'widget':self.photo_ref,'default':''}
key['additional_photos']={'widget':self.additional_photos,'default':''}

#visual assesment
key['surface_type']={'widget':self.surface_type,'default':'','items':['TSSC','HRA','SURFACE DRESSING','SLURRY SEAL','MICRO ASPHALT']}
