# coding=utf-8
from django.template import Context
from django.template.loader import get_template





TIMELINE = (
    {
        'image': '21_10_2016_stefan.png',
        'place': '21/10/2016 - Germany',
        'title': 'Annual conference of Federal Association of Free Radios',
        'location': 'Germany, Halle (Saale)',
        'speakers': 'Stefan Walluhn / Jan Langhammer',
        'resources': (
            render_german_flag(),
            render_link(title='Podcast', icon='volume-up', url='http://www.community-media.net/programmplanung-und-darstellung-mit-radioco/')
        )
    },
    {
        'image': '15_07_2016_iago_chema.png',
        'place': '15/07/2016 - Spain',
        'title': 'Escola de Verán de CUAC FM',
        'location': 'Spain, A Coruña',
        'speakers': 'Iago Veloso / José María Casanova',
        'resources': (
            render_galician_flag(),
            render_link(title='Web', icon='globe', url='https://cuacfm.org/escuela-verano-cuacfm-2016/'),
            '|',
            render_spanish_flag(),
            render_link(title='PDF', icon='pdf-o', url='/resources/campamento_veran_cuac.pdf')
        )
    },
    {
        'image': '12_03_2016_raspberry.png',
        'place': '12/03/2016 - Spain',
        'title': 'Segundo Encuentro Europeo de Medios Comunitarios',
        'location': 'Spain, Madrid',
        'speakers': 'José María Casanova / Álex Cortiñas',
        'resources': (

        )
    },
    {
        'image': '23_01_2016_kalimera_isa_alex.png',
        'place': '23/01/2016 - Spain',
        'title': 'Xornada de Ondas Libres e Comunitarias',
        'location': 'Spain, Santiago de Compostela',
        'speakers': 'Álex Cortiñas / Isabel Lema Blanco',
        'resources': (
            render_galician_flag(),
            render_link(title='PDF', icon='pdf-o', url='https://cuacfm.org/wp-content/uploads/2016/02/Kalimera-2015-g.pdf')

        )
    },
    {
        'image': '22_10_2015_isa_chema.png',
        'place': '22/10/2015 - Spain',
        'title': 'Xornada de Boas Prácticas de Software Libre para ONGs',
        'location': 'Spain, Santiago de Compostela',
        'speakers': 'Isabel Lema Blanco / José María Casanova Crespo',
        'resources': (
            render_galician_flag(),
            render_link(title='Video', icon='youtube-play', url='https://www.youtube.com/watch?v=gADKGwaHqC0')
        )
    },
    {
        'image': '05_06_2015_captcha2.png',
        'place': '05/06/2015 - Germany',
        'title': 'Radio Archives in European Community Media',
        'location': 'Germany, Halle (Saale)',
        'speakers': 'Jose Maria Casanova / Fernando Souto',
        'resources': (
            render_english_flag(),
            render_link(title='PDF', icon='pdf-o', url='https://cuacfm.org/wp-content/uploads/2015/06/CAPTCHA-2015-Livingarchives-From-manual-analogical-recording-to-RadioCo.pdf')
        )
    },
    {
        'image': '02_12_2014_iago.png',
        'place': '02/12/2014 - Spain, Ourense',
        'title': '14th edition of Technological Projects',
        'location': 'Spain, Ourense',
        'speakers': 'Iago Veloso',
        'resources': (
            render_spanish_flag(),
            render_link(title='PDF', icon='pdf-o', url='/presentacion-expourense.pdf')
        )
    },
    {
        'image': '17_10_2014_iago.png',
        'place': '17/10/2014 - Spain',
        'title': 'VII edition of Best Final Project with Free Software',
        'location': 'Spain, Santiago de Compostela',
        'speakers': 'Iago Veloso',
        'resources': (
            render_galician_flag(),
            render_link(title='PDF', icon='pdf-o', url='/resources/mancomun_radioco.pdf.pdf')
        )
    },
    {
        'image': '15_09_2014_fic.png',
        'place': '15/09/2014 - Spain',
        'title': 'Project exposition',
        'location': 'Spain, A Coruña',
        'speakers': 'Iago Veloso',
        'resources': (
            render_spanish_flag(),
            render_link(title='PDF 1', icon='pdf-o', url='/resources/VelosoAbalo_Iago_TFG_2014.pdf'),
            render_link(title='PDF 2', icon='pdf-o', url='/resources/presentacion.pdf')
        )
    },
    {
        'image': '13_04_2014_encuentro14.png',
        'place': '13/04/2014 - Spain',
        'title': 'Encuentro 14',
        'location': 'Spain, A Coruña',
        'speakers': 'Iago Veloso',
        'resources': ()
    },

)


STATIONS = (
    {
        'name': 'Radio Corax',
        'image': 'corax-solo-logo.png',
        'location': 'Germany, Halle',
        'description': 'Radio Corax is a non-commercial radio available in Halle and in southern Saxony-Anhalt on the VHF frequency 95.9 MHz. Affiliations: BFR, CMFE, AMARC',
        'resources': (
            render_link(title='Web', icon='globe', url='http://radiocorax.de/'), #style="background-color: rgb(241, 139, 109);"
        )
    },
    {
        'name': 'Cuac FM',
        'image': 'cuac-1.png',
        'location': 'Germany, Halle',
        'description': 'Cuac FM is a community radio station that began broadcasting in 1996 on 103.4 FM in A Coruña, Spain. Affiliations: AMARC, ReMC, ReGarLiC',
        'resources': (
            render_link(title='Web', icon='globe', url='https://cuacfm.org/'), #style="background-color: #DD9933;
        )
    }
)


TEAM = (
    {
        'name': 'Víctor Tojo',
        'image': 'victor_tojo.jpg',
        'role': 'Designer',
        'description': 'RadioCo trademark design',
        'resources': (
            render_link(title='Web', icon='globe', url='http://victortojo.com/'),
        )
    }
)
