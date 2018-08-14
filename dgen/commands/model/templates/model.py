class MyModel(models.Model):
    class Meta:
        verbose_name = _('MyModel')
        verbose_name_plural = _('MyModels')
        ordering = ['id']

    def __str__(self):
        return f'MyModel{self.id}'
