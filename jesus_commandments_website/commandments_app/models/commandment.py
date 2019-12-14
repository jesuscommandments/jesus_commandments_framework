from django.db import models
from django.utils import translation
from froala_editor.fields import FroalaField

from commandments_app.models import CommandmentCategories


class CommandmentManager(models.Manager):
    def with_background(self):
        return (c for c in Commandment.objects.all().prefetch_related('drawing_set') if c.background_drawing())


class Commandment(models.Model):
    title = models.CharField(max_length=256)
    title_negative = models.CharField(max_length=256, default='', blank=True)
    devotional = FroalaField(blank=True, null=True)
    devotional_source = models.CharField(max_length=256, default='', blank=True, null=True)
    category = models.CharField(max_length=32,
                                choices=[(tag.name, tag.value) for tag in CommandmentCategories],
                                default=CommandmentCategories.Salvation)
    quote = models.TextField(default='', blank=True, null=True)
    quote_source = models.CharField(max_length=256, default='', blank=True, null=True)
    bible = None
    languages = [translation.get_language()]
    objects = CommandmentManager()

    def primary_bible_reference(self):
        """ Primary references is the first found unique reference according to the words of Jesus,
        directly related to the commandment. """
        reference = self.primarybiblereference
        reference.set_bible(self.bible)
        return reference

    def direct_bible_references(self):
        """ Extra direct Bible references which expands or explain the same commandment. """
        return self._get_translated_bible_references(self.directbiblereference_set.all())

    def indirect_bible_references(self):
        """ Extra, more indirect Bible references, relating to the same commandment. """
        return self._get_translated_bible_references(self.indirectbiblereference_set.all())

    def duplicate_bible_references(self):
        """ Another Bible reference to more or less the same as the primary, direct or indirect, 
        with not much new information, although it will confirm the same Bible references. """
        return self._get_translated_bible_references(self.duplicatebiblereference_set.all())

    def example_bible_references(self):
        """ In these Bible references you will find examples and testimonies how this commandment  
        is being executed. """
        return self._get_translated_bible_references(self.examplebiblereference_set.all())

    def study_bible_references(self):
        """ Extra Bible references (most often larger parts of Bible books) which are good for 
        extra study on this commandment. """
        return self._get_translated_bible_references(self.studybiblereference_set.all())

    def background_drawing(self):
        return self.drawings()[0] if self.drawings() else ''

    def background_song(self):
        return self.songs()[0] if self.songs() else ''

    def drawings(self):
        # This is actually faster than filter in in the query,
        # as prefetch_related can be used if we do all() instead of filter()
        return [d for d in self.drawing_set.all() if d.is_public]

    def songs(self):
        return self._filter_on_language(self.song_set)

    def superbooks(self):
        return [d for d in self.superbook_set.all() if d.is_public]

    def movies(self):
        return self._filter_on_language(self.movie_set)

    def short_movies(self):
        return self._filter_on_language(self.shortmovie_set)

    def sermons(self):
        return self._filter_on_language(self.sermon_set)

    def pictures(self):
        return self.picture_set.filter(is_public=True)

    def testimonies(self):
        return self._filter_on_language(self.testimony_set)

    def blogs(self):
        return self._filter_on_language(self.blog_set)

    def books(self):
        return self._filter_on_language(self.book_set)

    def questions(self):
        return self.question_set.all()

    def _filter_on_language(self, query):
        filter_languages = ['any'] + self.languages
        return query.filter(language__in=filter_languages, is_public=True)

    def _get_translated_bible_references(self, query_set):
        sorted_query_set = sorted(query_set)
        [ref.set_bible(self.bible) for ref in sorted_query_set]
        return sorted_query_set

    def __str__(self):
        return self.title
