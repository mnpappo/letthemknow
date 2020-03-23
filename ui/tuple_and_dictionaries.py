STATE_LIST = ((1, 'I am Safe'),
              (2, 'I am Panicked!'),
              (3, 'I am Affected!!'))

DIVISION_LIST = (('dhaka', 'Dhaka'),
                 ('chittagong', 'Chittagong'),
                 ('barisal', 'Barisal'),
                 ('khulna', 'Khulna'),
                 ('mymensingh', 'Mymensingh'),
                 ('rajshahi', 'Rajshahi'),
                 ('rangpur', 'Rangpur'),
                 ('sylhet', 'Sylhet'),
                 )


division_code_dic = {
    'Barisal': 'BD-A',
    'Chittagong': 'BD-B',
    'Dhaka': 'BD-C',
    'Khulna': 'BD-D',
    'Mymensingh': 'BD-H',
    'Rajshahi': 'BD-E',
    'Rangpur': 'BD-F',
    'Sylhet': 'BD-G',
    }

district_code_dic = {
    'Bagerhat': 'BD-05',
    'Bandarban': 'BD-01',
    'Barguna': 'BD-02',
    'Barisal': 'BD-06',
    'Bhola': 'BD-07',
    'Bogra': 'BD-03',
    'Brahmanbaria': 'BD-04',
    'Chandpur': 'BD-09',
    'Chapai Nawabganj': 'BD-45',
    'Chittagong': 'BD-10',
    'Chuadanga': 'BD-12',
    'Comilla': 'BD-08',
    'Cox\'s Bazar': 'BD-11',
    'Dhaka': 'BD-13',
    'Dinajpur': 'BD-14',
    'Faridpur': 'BD-15',
    'Feni': 'BD-16',
    'Gaibandha': 'BD-19',
    'Gazipur': 'BD-18',
    'Gopalganj': 'BD-17',
    'Habiganj': 'BD-20',
    'Jamalpur': 'BD-21',
    'Jessore': 'BD-22',
    'Jhalakathi': 'BD-25',
    'Jhenaidah': 'BD-23',
    'Joypurhat': 'BD-24',
    'Khagrachhari': 'BD-29',
    'Khulna': 'BD-27',
    'Kishoreganj': 'BD-26',
    'Kurigram': 'BD-28',
    'Kushtia': 'BD-30',
    'Lakshmipur': 'BD-31',
    'Lalmonirhat': 'BD-32',
    'Madaripur': 'BD-36',
    'Magura': 'BD-37',
    'Manikganj': 'BD-33',
    'Meherpur': 'BD-39',
    'Moulvibazar': 'BD-38',
    'Munshiganj': 'BD-35',
    'Mymensingh': 'BD-34',
    'Naogaon': 'BD-48',
    'Narail': 'BD-43',
    'Narayanganj': 'BD-40',
    'Narsingdi': 'BD-42',
    'Natore': 'BD-44',
    'Netrakona': 'BD-41',
    'Nilphamari': 'BD-46',
    'Noakhali': 'BD-47',
    'Pabna': 'BD-49',
    'Panchagarh': 'BD-52',
    'Patuakhali': 'BD-51',
    'Pirojpur': 'BD-50',
    'Rajbari': 'BD-53',
    'Rajshahi': 'BD-54',
    'Rangamati': 'BD-56',
    'Rangpur': 'BD-55',
    'Satkhira': 'BD-58',
    'Shariatpur': 'BD-62',
    'Sherpur': 'BD-57',
    'Sirajganj': 'BD-59',
    'Sunamganj': 'BD-61',
    'Sylhet': 'BD-60',
    'Tangail': 'BD-63',
    'Thakurgaon': 'BD-64',
}

district_division_dic = {
    'BD-05': 'BD-D',
    'BD-01': 'BD-B',
    'BD-02': 'BD-A',
    'BD-06': 'BD-A',
    'BD-07': 'BD-A',
    'BD-03': 'BD-E',
    'BD-04': 'BD-B',
    'BD-09': 'BD-B',
    'BD-45': 'BD-E',
    'BD-10': 'BD-B',
    'BD-12': 'BD-D',
    'BD-08': 'BD-B',
    'BD-11': 'BD-B',
    'BD-13': 'BD-C',
    'BD-14': 'BD-F',
    'BD-15': 'BD-C',
    'BD-16': 'BD-B',
    'BD-19': 'BD-F',
    'BD-18': 'BD-C',
    'BD-17': 'BD-C',
    'BD-20': 'BD-G',
    'BD-21': 'BD-H',
    'BD-22': 'BD-D',
    'BD-25': 'BD-A',
    'BD-23': 'BD-D',
    'BD-24': 'BD-E',
    'BD-29': 'BD-B',
    'BD-27': 'BD-D',
    'BD-26': 'BD-C',
    'BD-28': 'BD-F',
    'BD-30': 'BD-D',
    'BD-31': 'BD-B',
    'BD-32': 'BD-F',
    'BD-36': 'BD-C',
    'BD-37': 'BD-D',
    'BD-33': 'BD-C',
    'BD-39': 'BD-D',
    'BD-38': 'BD-G',
    'BD-35': 'BD-C',
    'BD-34': 'BD-H',
    'BD-48': 'BD-E',
    'BD-43': 'BD-D',
    'BD-40': 'BD-C',
    'BD-42': 'BD-C',
    'BD-44': 'BD-E',
    'BD-41': 'BD-H',
    'BD-46': 'BD-F',
    'BD-47': 'BD-B',
    'BD-49': 'BD-E',
    'BD-52': 'BD-F',
    'BD-51': 'BD-A',
    'BD-50': 'BD-A',
    'BD-53': 'BD-C',
    'BD-54': 'BD-E',
    'BD-56': 'BD-B',
    'BD-55': 'BD-F',
    'BD-58': 'BD-D',
    'BD-62': 'BD-C',
    'BD-57': 'BD-H',
    'BD-59': 'BD-E',
    'BD-61': 'BD-G',
    'BD-60': 'BD-G',
    'BD-63': 'BD-C',
    'BD-64': 'BD-F',
}
