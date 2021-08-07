import pygame
import sys
import button

pygame.init()

pygame.font.init()

clock = pygame.time.Clock()

surface = pygame.display.set_mode((1777, 1000))

pygame.display.set_caption("Encontre sua rota!")

vertices = ['Aaiun, Western Sahara', 'Aalborg, Denmark', 'Abenra, Denmark', 'Aberdeen, Scotland', 'Aarhus, Denmark', 'Abadan, Iran', 'Abu Dhabi, United Arab', 'Accra, Ghana', 'Acajutla, El Salvador', 'Abidjan, Ivory Coast', 'Acapulco, Mexico', 'Ad Damman, Saudi', 'Aden, Yemen', 'Agadir, Morocco', 'Al Manamah, Bahrain', 'Ajaccio, Corsica', 'Akita, Japan', 'Akureyri, Iceland', 'Al Basrah, Iraq', 'Al Jubayl, Saudi Arabia', 'Albany, Australia', 'Albany, New York, U.S.A.', 'Al Latakia, Syria', 'Al Aqabah, Jordan', 'Aleksandrovsksakhalinskiy, Russia', 'Alesund, Norway', 'Alicante, Spain', 'Alexandria, Egypt', 'Algeciras, Spain', 'Algiers, Algeria', 'Almeria, Spain', 'Almirante, Panama', 'Altagracia, Venezuela', 'Amagasaki, Japan', 'Amapala, Honduras', 'Ambon, Indonesia', 'Amlwch, Wales', 'Ancona, Italy', 'Anecho, Togo', 'Amuay, Venezuela', 'Washington, U.S.A.', 'Anan, Japan', 'Ango Ango, Congo', 'Angra Dos Reis, Brazil', 'Annaba, Algeria', 'Annapolis, Maryland,', 'Antalya, Turkey', 'Antofagasta, Chile', 'Antwerp, Belgium', 'Antibes, France', 'Antilla, Cuba', 'Aparri, Philippines', 'Aomori, Japan', 'Apapa, Nigeria', 'Apia, Samoa', 'Apra, Guam, Mariana Islands', 'Apra, Guam, Mariana', 'Arbatax, Italy', 'Ardrossan, Scotland', 'Arendal, Norway', 'Argentia, Canada', 'Argostolion, Greece', 'Arica, Chile', 'Aracaju, Brazil', 'Ashdod, Israel', 'Arzew, Algeria', 'As Salif, Yemen', 'Assab, Ethiopia', 'As Sukhayrah, Tunisia', 'Ash Shuwaykh, Kuwait', 'Assens, Denmark', 'Astoria, Oregon, U.S.A.', 'Atucha, Argentina', 'Atumi, Japan', 'Au-Ao Chaing, Taiwan', 'Auckland, New Zealand', 'Augusta, Sicily', 'Avarua, Cook Islands', 'Aveiro, Portugal', 'Aviles, Spain', 'Ayn Sukhnah, Egypt', 'Az Zarqa Island, United', 'Bachaquero, Venezuela', 'Bagnoli, Italy', 'Avonmouth, England', 'Ayios Nikolaos, Greece', 'Bahia Honda, Cuba', 'Baker Island, North', 'Balboa, Panama', 'Kalimantan, Indonesia', 'Baltimore, Maryland,', 'Banana, Congo', 'Bandar Abbas, Iran', 'Bandar Al Mishab, Saudi', 'Bandar Khomeini, Iran', 'Banes, Cuba', 'Banghazi, Libya', 'Bangkok, Thailand', 'Baniyas, Syria', 'Banzart, Tunisia', 'Banjul, Gambia', 'Bantry Bay, Ireland', 'Bar, Montenegro', 'Baracoa, Cuba', 'Barahona, Dominican', 'Barbers Point, Hawaii,', 'Barcelona, Spain', 'Barcelona, Venezuela', 'Basseterre, Saint Kitts', 'Bastia, Corsica', 'Bari, Italy', 'Barry, Wales', 'Basra, Iraq', 'Bassein, Burma', 'Basuo Gang, China', 'Bata, Equatorial Guinea', 'Bassens, France', 'Batangas, Luzon,', 'Bath, Maine, U.S.A.', 'Baton Rouge, Louisiana, U.S.A.', 'Baton Rouge, Louisiana,', 'Bayonne, France', 'Bayonne, New Jersey,', 'Beihai, China', 'Beira, Mozambique', 'Beirut, Lebanon', 'Baytown, Texas, U.S.A.', 'Beaumont, Texas, U.S.A.', 'Bee Ness, England', 'Bejaia, Algeria', 'Belawan, Indonesia', 'Belem, Brazil', 'Belfast, Northern', 'Belize, Belize', 'Belomorsk, Russia', 'Benicia, California,', 'Berbera, Somalia', 'Bergen, Norway', 'Bhavnagar, India', 'Bikini, Marshall', 'Bilbao, Spain', 'Bishop Rock, England', 'Bishop Rock, England *', 'Bissau, Guinea-Bissau', 'Blyth, England', 'Boca De Tanamo, Cuba', 'Boca Grande, Florida,', 'Bjornoya, Svalbard', 'Blaye, France', 'Bluff Harbor, New', 'Bodo, Norway', 'Bohang, South Korea', 'Boma, Congo', 'Bombay, India', 'Bonny, Nigeria', 'Bordeaux, France', 'Boston, Massachusetts,', 'Botas, Turkey', 'Botwood, Canada', 'Boulogne, France', 'Bowen, Australia', 'Brake, Germany', 'Terminal), Nigeria', 'Bremen, Germany', 'Bremerhaven, Germany', 'Brest, France', 'Brevik, Norway', 'Bowling, Scotland', 'Connecticut, U.S.A.', 'Bridgetown, Barbados', 'Brighton, Trinidad', 'Brisbane, Australia', 'Brindisi, Italy', 'Bristol, England', 'Brugge, Belgium', 'Brunswick, Georgia,', 'Brixham, England', 'Brooklyn, New York,', 'Broome, Australia', 'Brussels, Belgium', 'Bruxelles, Belgium', 'Buchanan, Liberia', 'Brownsville, Texas,', 'Buckner Bay, Okinawa', 'Jima, Ryukyu Islands', 'Buenos Aires, Argentina', 'Kuril Islands, Russia', 'Bunbury, Australia', 'Bundaberg, Australia', 'Bur Ibrahim, Egypt', 'Bur Safaga, Egypt', 'Burea, Sweden', 'Burgas, Bulgaria', 'Burnside, Louisiana,', 'Burutu, Nigeria', 'Busan, South Korea', 'Bushehr, Iran', 'Cabedelo, Brazil', 'Cabimas, Venezuela', 'Cabinda, Cabinda', 'Cadiz, Spain', 'Cagliari, Sardinia', 'Cairn Ryan, Scotland', 'Caen, France', 'Caibarien, Cuba', 'Calabar, Nigeria', 'Calais, France', 'Calcutta, India', 'Caldera, Chile', 'Calicut, India', 'Callao, Peru', 'Campeche, Mexico', 'Camden, New Jersey,', 'Canakkle, Turkey', 'Camp Lloyd, Greenland', 'Cannes, France', 'Campana, Argentina', 'Hawbesburg), Canada', 'End), Massachusetts,', 'Cap-Haitien, Haiti', 'Cape Lopez, Gabon', 'Cape St. Jacques, Vietnam', 'Cape Town, South', 'Cardenas, Cuba', 'Cardiff, Wales', 'Caripito, Venezuela', 'Carmen, Mexico', 'Cartagena, Colombia', 'Cartagena, Spain', 'Casablanca, Morocco', 'Castries, St. Lucia', 'Castro-Urdiales, Spain', 'Catania, Sicily', 'Casilda, Cuba', 'Castellon, Spain', 'Cayman Brac, Cayman', 'Cebu, Philippines', 'Ceuta, Morocco', 'Charleston, South', 'Carolina, U.S.A.', 'Chah Bahar, Iran', 'Chalna, Mungla', 'Anchorage, Bangladesh', 'Chanaral, Chile', 'Charlotte Amalie, St.', 'Thomas, Virgin Islands', 'Chatham, Canada', 'Chatham, England', 'Chen-Chang, China', 'Cherbourg, France', 'Chi-Lung, Taiwan', 'Chibai, Japan', 'Chicoutimi, Canada', 'Chimbote, Peru', 'Chimu Wan, Okinawa', 'Ching-Tao, China', 'Chin-Huang-Tao, China', 'Chin Hai, South Korea', 'Chinnampo, North', 'Chioggia, Italy', 'Chongjin, North Korea', 'Christiansted, St. Croix', 'Christmas Island, Line Islands', 'Christmas Island, Line', 'Churchill, Canada', 'Cienfuegos, Cuba', 'Civitavecchia, Italy', 'Coatzacoalcos, Mexico', 'Cochin, India', 'Colombo, Sri Lanka', 'Cobh, Ireland', 'Colon, Panama', 'Colonia, Uruguay', 'Conchan, Peru', 'Constanta, Romania', 'Conakry, Guinea', 'Contrecoeur, Canada', 'Coos Bay, Oregon, U.S.A.', 'Copenhagen, Denmark', 'Coquimbo, Chile', 'Cordova, Alaska, U.S.A.', 'Cork, Ireland', 'Corner Brook, Canada', 'Corinto, Nicaragua', 'Corpus Christi, Texas,', 'Corunna, Spain', 'Cotonou, Benin', 'Courtenay Bay, New', 'Brunswick, Canada', 'Covenas, Colombia', 'Cowes, England', 'Cristobal, Panama', 'Cuxhaven, Germany', 'Dagu, China', 'Dagu Bar, China', 'Dakar, Senegal', 'Dalhousie, Canada', 'Dalian, China', 'Dalien, China', 'Danang, Vietnam', 'Dar Es Salaam, Tanzania', 'Dartmouth, England', 'Darwin, Australia', 'Das Island, United Arab', 'Davao, Philippines', 'Deepwater Point, New', 'Jersey, U.S.A.', 'Delfzijl, Netherlands', 'Derince, Turkey', 'Devonport, England', 'Dieppe, France', 'Digby, Canada', 'Dikson, Russia', 'Dover, England', 'Dhekelia, Cyprus', 'Djibouti, Djibouti', 'Diamante, Argentina', 'Diego Garcia, Chagos', 'Dubrovnik, Croatia', 'Donges, France', 'Douala, Cameroon', 'Douglas, Isle Of Man', 'Dublin, Ireland', 'Dudinka, Russia', 'Dumai, Indonesia', 'Dun Laoghaire, Ireland', 'Dundee, Scotland', 'Dunedin, New Zealand', 'Durban, South Africa', 'Durres, Albania', 'Dunkerque, France', 'Dutch Harbor, Alaska,', 'East London, South', 'Easter Island, South', 'Egersund, Norway', 'Eilat, Israel', 'El Aaiun, Western', 'El Jadida, Morocco', 'Esbjerg, Denmark', 'Esmeraldas, Ecuador', 'El Segundo, California,', 'Eniwetak, Marshall', 'Ensenada, Mexico', 'Emden, Germany', 'Escravos, Nigeria', 'Esperance, Australia', 'Ensted, Denmark', 'Es Sider, Libya', 'Eureka, California,', 'Everett, Washington,', 'Faaborg, Denmark', 'Faborg, Denmark', 'Famagusta, Cyprus', 'Fanning Island, North', 'Farge, Germany', 'Massachusetts, U.S.A.', 'Farsund, Norway', 'Falmouth, England', 'Faslane Bay, Scotland', 'Fastnet Rock, Ireland*', 'Fateh Terminal, United', 'Fecamp, France', 'Felixstowe, England', 'Felton, Cuba', 'Fernandina, Florida,', 'Fethiye, Turkey', 'Figuera Da Foz, Portugal', 'Fleetwood, England', 'Flekkefjorden, Norway', 'Fishguard, Wales', 'Fiumicino, Italy', 'Flensburg, Germany', 'Florida Straits, U.S.A.', 'Terminal, Nigeria', 'Flushing, Netherlands', 'Florida, U.S.A.', 'Fort-Liberate, Haiti', 'Fortaleza, Brazil', 'Fray Bentos, Uruguay', 'Fredericia, Denmark', 'Frederiksted, St. Croix', 'Fredrikstad, Norway', 'Freeport, Bahamas', 'Freetown, Sierra Leone', 'Fremantle, Australia', 'Fu-Chou, China', 'Fujayrah, United Arab', 'Funafuti, Tuvalu', 'Funchal, Madeira', 'Fuzhou, China', 'Gaeta, Italy', 'Galeota Point, Trinidad', 'Galway, Ireland', 'Gdansk, Poland', 'Geelong, Australia', 'Gela, Italy', 'Gamba, Gabon', 'Galle, Sri Lanka', 'Gallipoli, Italy', 'Galveston, Texas, U.S.A.', 'Gavle, Sweden', 'Gdynia, Poland', 'Gebe Island, Indonesia', 'Gelibolu, Turkey', 'Gemlick, Turkey', 'Genova, Italy', 'Georgetown, Guyana', 'Geraldton, Australia', 'Ghazaouet, Algeria', 'Ghent, Belgium', 'Gibara, Cuba', 'Gijon, Spain', 'Gizan, Saudi Arabia', 'Gladstone Harbor, Australia', 'Gonaives, Haiti', 'Good Hope, Louisiana,', 'Goole, England', 'Glasgow, Scotland', 'Goose Bay, Canada', 'Gloucester, England', 'Godhavn, Greenland', 'Godthab, Greenland', 'Golcuk, Turkey', 'Golfito, Costa Rica', 'Grena, Denmark', 'Grimsby, England', 'Grimstad, Norway', 'Goteborg, Sweden', 'Granton, Scotland', 'Granville, France', 'Groton, Connecticut,', 'Guanica, Puerto Rico', 'Guanta, Venezuela', 'Gravesend, England', 'Gothenburg, Sweden', 'Greenock, Scotland', 'Gove Harbor, Australia', 'Greenville, Liberia', 'Guantanamo, Cuba', 'Guayaquil, Ecuador', 'Guaymas, Mexico', 'Guiria, Venezuela', 'Gulfport, Mississippi,', 'Gunsan, South Korea', 'Habana, Cuba', 'Hachinohe, Japan', 'Haderslev, Denmark', 'Haifa, Israel', 'Haines, Alaska, U.S.A.', 'Haiphong, Vietnam', 'Hakata, Japan', 'Hakodate, Japan', 'Hakonsvern, Norway', 'Haldia, India', 'Halifax, Canada', 'Halmstad, Sweden', 'Hamburg, Germany', 'Hamilton, Bermuda', 'Hamina, Finland', 'Halsingborg, Sweden', 'Halul Island, Qatar', 'Hammerfest, Norway', 'Hankou, China', 'Harstad, Norway', 'Hartlepool, England', 'Harwich, England', 'Virginia, U.S.A.', 'Hamra, Egypt', 'Hango, Finland', 'Havana, Cuba', 'Helsingborg, Sweden', 'Helsingor, Denmark', 'Higashi-Iwase, Japan', 'Hilo, Hawaii, U.S.A.', 'Helsinki, Finland', 'Heysham, England', 'Hiroshima, Japan', 'Hirtshals, Denmark', 'Ho Chi Minh, Vietnam', 'Hobart, Tasmania', 'Hoboken, New Jersey,', 'Holyhead, Wales', 'Honawar, India', 'Honfleur, France', 'Hong Kong, China', 'Honiara, Solomon', 'Honolulu, Hawaii, U.S.A.', 'Honshu, Japan*', 'Hornefors, Sweden', 'Horsens, Denmark', 'Horten, Norway', 'Hososima Ko, Japan', 'Houston, Texas, U.S.A.', 'Horta, Fayal, Azores', 'Hsia-Men, China', 'Hua-Lien Kang, Taiwan', 'Huang-Pu, China', 'Huang Pu, China', 'Hudiksvall, Sweden', 'Huelva, Spain', 'Hueneme, California,', 'Hull, England', 'Hungnam, North Korea', 'Husnes, Norway', 'Hvalfjordhur, Iceland', 'Hyeres, France', 'Igarka, Russia', 'Ijmuiden, Netherlands', 'Ilo, Peru', 'Iloilo, Panay,', 'Iligan, Philippines', 'Imabari, Japan', 'Immingham, England', 'Incheon, South Korea', 'Inishtrahull, Ireland', 'Inishtrahull, Ireland*', 'Invergordon, Scotland', 'Inverness, Scotland', 'Ipswich, England', 'Iquique, Chile', 'Iraklion, Kriti', 'Isabel De Sagua, Cuba', 'Isabel Segunda, Isla De', 'Vieques, Puerto Rico', 'Iskenderun, Turkey', 'Isla De Pascua, South', 'Istanbul, Turkey', 'Itozakicho, Japan', 'Ivittuut, Greenland', 'Iwakuni, Japan', 'Izmir, Turkey', 'Jacksonville, Florida,', 'Jakarta, Indonesia', 'Jakobshavn, Greenland', 'Jakobstad, Finland', 'Jaluit, Marshall', 'Jarvis Island, Line', 'Jazireh-Ye Lavan, Iran', 'Jazireh-Ye Sirri, Iran', 'Jinhae, South Korea', 'Johnston Island, North', 'Jolo, Philippines', 'Jiddah, Saudi Arabia', 'Juneau, Alaska, U.S.A.', 'Kagoshima, Japan', 'Kahului, Maui, Hawaii,', 'Jubail, Saudi Arabia', 'Jucaro, Cuba', 'Jersey City, New Jersey,', 'Kakinada, India', 'Kalamai, Greece', 'Kali Limenes, Kriti,', 'Kaliningrad, Russia', 'Kalmar, Sweden', 'Kalundborg, Denmark', 'Kamaishi, Japan', 'Kankesanturai, Sri', 'Kamsar, Guinea', 'Kandalaksha, Russia', 'Kandla, India', 'Kaneohe Bay, Hawaii,', 'Karachi, Pakistan', 'Kardeljevo, Croatia', 'Karlshamn, Sweden', 'Karlskrona, Sweden', 'Kashima Ko, Japan', 'Kaunakakai, Hawaii, U.S.A.', 'Kenitra, Morocco', 'Kerch, Georgia', 'Kaunakakai, Hawaii,', 'Kavala, Greece', 'Keret, Russia', 'Kerkira, Greece', 'Kawasaki, Japan', 'Keelung, Taiwan', 'Keflavik, Iceland', 'Ketchikan, Alaska,', 'Key West, Florida, U.S.A.', 'Khalkis, Greece', 'Kharg Island, Iran', 'Khawr-Al-Amaya, Iraq', 'Kholmsk, Sakhalin,', 'Khorramshahr, Iran', 'Kiel, Germany', 'Kiire, Japan', 'Kimchaek, North Korea', 'Kin Wan, Japan', 'Kingston, Jamaica', 'Kismaayo, Somalia', 'Kitimat, Canada', 'Kingstown, St. Vincent', 'Kinuura, Japan', 'Kirkenes, Norway', 'Kiska, Alaska, U.S.A.', 'Klaipeda, Lithuania', 'Klaksvig, Faroe', 'Kobe, Japan', 'Kobenhavn, Denmark', 'Kochi, Japan', 'Kodiak, Alaska, U.S.A.', 'Kolding, Denmark', 'Koge, Denmark', 'Kokkola, Finland', 'Kokura, Japan', 'Kole, Cameroon', 'Komatsushima, Japan', 'Koniya, Ryukyu Islands', 'Koper, Slovenia', 'Korsakov, Sakhalin,', 'Kotka, Finland', 'Kristiansand, Norway', 'Kunsan, Japan', 'Kovda, Russia', 'Kpeme, Togo', 'Kure, Japan', 'Kristiansund, Norway', 'Kwa Ibo, Nigeria', 'Kushiro, Japan', 'Korsor, Denmark', 'Kragero, Norway', 'Kristinestad, Finland', 'Kyndby, Denmark', 'Kralendijk, Bonaire', 'Kribi, Cameroon', 'Kung Thep, Thailand', 'Kuching, Sarawak', 'Kyomipo, North Korea', 'La Ceiba, Honduras', 'La Guaira, Venezuela', 'La Habana, Cuba', 'La Isabel De Sagua, Cuba', 'La Rochelle, France', 'La Libertad, Ecuador', 'La Romana, Dominican', 'La Nouvelle, France', 'La Pallice, France', 'La Pampilla, Peru', 'La Plata, Argentina', 'La Libertad, El', 'La Salina, Venezuela', 'La Spezia, Italy', 'La Union, El Salvador', 'Lagos, Nigeria', 'Louisiana, U.S.A.', 'Larnaca, Cyprus', 'Larne, England', 'Lae, Papua New Guinea', 'Land Skrona, Sweden', 'Las Piedras, Venezuela', 'Latchi, Cyprus', 'Launceston, Tasmania', 'Lautoka Harbor, Fiji', 'Larvik, Norway', 'Las Palmas, Canary', 'Lavan Island, Iran', 'Lazaro Cardenas, Mexico', 'Le Havre, France', 'Le Verdon, France', 'Leith, Scotland', 'Les Cayes, Haiti', 'Leixoes, Portugal', 'Lerwick, Scotland', 'Libreville, Gabon', 'Lesnoy, Russia', 'Levuka, Fiji Islands', 'Licata, Sicily, Italy', 'Lien-Yun, China', 'Lillesand, Norway', 'Lianyungang, China', 'Limassol, Cyprus', 'Limerick, Ireland', 'Limetree Bay, St. Croix,', 'Limhamn, Sweden', 'Limon, Costa Rica', 'Lingkas, Kalimantan,', 'Lisboa, Portugal', 'Lisbon, Portugal', 'Little Creek, Virginia,', 'Liverpool, Canada', 'Liverpool, England', 'Livorno, Italy', 'Lobito, Angola', 'Lome, Togo', 'London, England', 'Long Beach, California,', 'Longji, Cameroon', 'Loop Terminal, Gulf Of', 'Mexico, U.S.A.', 'Lorient, France', 'California, U.S.A.', 'Lota, Chile', 'Lowestoft, England', 'Luanda, Angola', 'Lubeck, Germany', 'Lucinda, Australia', 'Lulea, Sweden', 'Lysekil, Sweden', 'Mackay, Australia', 'Mackenzie, Guyana', 'Madras, India', 'Mahon, Balearic', 'Maizuru, Japan', 'Majunga, Madagascar', 'Lyttelton, New', 'Maceio, Brazil', 'Magadan, Russia', 'Makassar, Sulawesi', 'Magallanes, Chile', 'Mahe, Seychelles', 'Malabo, Equatorial Guinea', 'Malabo, Equatorial', 'Malacca, Malaysia', 'Malaga, Spain', 'Maldogado, Uruguay', 'Malakal, Palau Islands', 'Manila, Philippines', 'Malmo, Sweden', 'Maltepe, Turkey', 'Manaus, Brazil', 'Manchester, England', 'Mandal, Norway', 'Manfredonia, Italy', 'Mangalore, India', 'Maniitsoq, Greenland', 'Manzanillo, Cuba', 'Maracaibo, Venezuela', 'Manzanillo, Mexico', 'Maputo, Mozambique', 'Pennsylvania, U.S.A.', 'Mariel, Cuba', 'Marin, Ponte Vedra Bay,', 'Marmagao, India', 'Marsaxlokk, Malta', 'Marseille, France', 'Masan, South Korea', 'Masbate, Philippines', 'Matanzas, Cuba', 'Masnedsund, Denmark', 'Massawa, Ethiopia', 'Matarani, Peru', 'Mayaquez, Puerto Rico', 'Mayport, Florida, U.S.A.', 'Mazatlan, Mexico', 'Matadi, Congo', 'Matagorda Bay, Texas,', 'Mathew Town, Great', 'Matruh, Egypt', 'Megara, Greece', 'Melbourne, Australia', 'Melilla, Morocco', 'Menton, France', 'Mersa Al Hamra, Egypt', 'Mersin, Turkey', 'Messina, Sicily, Italy', 'Mers El Kebir, Algeria', 'Methil, Scotland', 'Miami, Florida, U.S.A.', 'Middlefart, Denmark', 'Midway Island, North', 'Miike, Japan', 'Milazzo, Sicily, Italy', 'Mina Al Ahmadi, Kuwait', 'Milford Haven, Wales', 'Milner Bay, Australia', 'Mina Abd Allah, Kuwait', 'Mina Raysut, Oman', 'Mina Sulman, Bahrayn', 'Minatitlan, Mexico', 'Miragoane, Haiti', 'Misumi, Japan', 'Mitilini, Greece', 'Mina Saqr, United Arab', 'Mina Saud, Kuwait', 'Moa, Cuba', 'Mobile, Alabama, U.S.A.', 'Mocamedes, Angola', 'Moengo, Suriname', 'Mogadishu, Somalia', 'Mogpo, South Korea', 'Mohammedia, Morocco', 'Moi Rana, Norway', 'Moji, Japan', 'Mokpo, South Korea', 'Molde, Norway', 'Mon Falcone, Italy', 'Monaco, Monaco', 'Monopoli, Italy', 'Mombasa, Kenya', 'Monrovia, Liberia', 'Montego Bay, Jamaica', 'Montevideo, Uruguay', 'Montreal, Canada*', 'Mormugao, India', 'Montrose, Scotland', 'Mosjoen, Norway', 'Morehead City, North', 'Moss, Norway', 'Mosselbaai, South', 'Mosselbay, South', 'Mostaganem, Algeria', 'Mourilyan, Australia', 'Mtwara, Tanzania', 'Muroran, Japan', 'Murmansk, Russia', 'Mutrah, Oman', 'Naestved, Denmark', 'Nagasaki, Japan', 'Nagoya, Japan', 'Naha, Okinawa Jima,', 'Najkin, North Korea', 'Nakagusuku, Okinawa', 'Nakhodka, Russia', 'Naknek, Alaska, U.S.A.', 'Namsos, Norway', 'Nakskov, Denmark', 'Nampo, North Korea', 'Nan-Ching, China', 'Nanaimo, Canada', 'Naples, Italy', 'Napoli, Italy', 'Nanao, Japan', 'Nanchital, Mexico', 'Nanjing, China', 'Nanortalik, Greenland', 'Nantes, France', 'Napieir, New Zealand', 'Narvik, Norway', 'Nasipit, Philippines', 'Nassau, Bahama Islands', 'Navarino Bay, Greece', 'Navlakhi, India', 'Navplion, Greece', 'Negappattinam, India', 'Nelson, New Zealand', 'Natal, Brazil', 'New Mangalore, India', 'New Plymouth, New', 'New Orleans, Louisiana,', 'New York, New York,', 'Newark, New Jersey, U.S.A.', 'Newark, New Jersey,', 'Newcastle, Australia', 'Newport, Rhode Island,', 'Newport, Wales', 'Newcastle, Canada', 'Newcastle, England', 'Newport News, Virginia,', 'Nha Be, Vietnam', 'Nha Trang Bay, Vietnam', 'Nice, France', 'Niigata, Japan', 'Nome, Alaska, U.S.A.', 'Nikiski, Alaska, U.S.A.', 'Nordenham, Germany', 'Norfolk, Virginia, U.S.A.', 'Norrkoping, Sweden', 'Noumea, New Caledonia', 'Novorossiysk, Russia', 'Nueva Gerona, Cuba', 'Nueva Palmira, Uruguay', 'Nuevitas, Cuba', 'Nukualofa, Tonga', 'Nykobing, Denmark', 'Oakland, California,', 'Ocean Island, Pacific', 'Odense, Denmark', 'Odessa, Ukraine', 'Oita, Japan', 'Okha, India', 'Okha, Sakhalin, Russia', 'Olbia, Sardinia', 'Olongapo, Philippines', 'Olympia, Washington,', 'Onega, Russia', 'Oostende, Belgium', 'Oporto, Portugal', 'Opua, New Zealand', 'Oran, Algeria', 'Orange, Texas, U.S.A.', 'Oranjestad, Aruba', 'Oranjestad, St.', 'Ormos Soudhas, Kriti', 'Ornskoldsvik, Sweden', 'Osaka, Japan', 'Oslo, Norway', 'Ostrica, Louisiana, U.S.A.', 'Otago Harbor, New', 'Otaru, Japan', 'Ouessant, Ile De France', 'Oulu, Finland', 'Oxelosund, Sweden', 'Padang, Indonesia', 'Pago Pago, American', 'Palembang, Indonesia', 'Palermo, Sicily, Italy', 'Palm Beach, Florida,', 'Palma, Balearic Islands', 'Palma, Balearic', 'Palua, Venezuela', 'Panama, Panama*', 'Panamburu, India', 'Panjang, Indonesia', 'Pansio, Finland', 'Papeete, Tahiti, French', 'Paradip, India', 'Paramaribo, Suriname', 'Paranagua, Brazil', 'Paranam, Suriname', 'Parrsboro, Canada', 'Paulillac, France', 'Pearl Harbor, Hawaii,', 'Pasadena, Texas, U.S.A.', 'Pascagoula, Mississippi,', 'Pechenga, Russia', 'Penarth, Wales', 'Patrai, Greece', 'Pei-Hai, China', 'Pemba, Mozambique', 'Penang, Malaysia', 'Pensacola, Florida,', 'Pepel, Sierra Leone', 'Perth, Australia', 'Petersburg, Alaska,', 'Petropavlovskkamchatskiy, Russia', 'Pevek, Russia', 'Phnom Penh, Cambodia', 'Phuket, Thailand', 'Pimentel, Peru', 'Pina, Panama', 'Piraievs, Greece', 'Pisagua, Chile', 'Pitea, Sweden', 'Ploce, Croatia', 'Pohang, South Korea', 'Point Comfort, Texas,', 'Pointe Noire, Congo', 'Plymouth, England', 'Pisco, Peru', 'Plymouth, Montserrat', 'Polyarnyy, Russia', 'Ponape, Caroline', 'Ponce, Puerto Rico', 'Poole, England', 'Port Alice, Canada', 'Porkkala, Finland', 'Ponta Delgada, Azores', 'Porlamar, Margarita,', 'Port Antonio, Jamaica', 'Port Arthur, Texas,', 'Port Au Prince, Haiti', 'Port Blair, Andaman', 'Port Castries, St. Lucia', 'Port Chalmers, New', 'Port Darwin, Australia', 'Port Des Galets, Reunion Island', 'Port Kelang, Malaysia', 'Port Kembla, Australia', 'Port Lavaca, Texas,', 'Port Kamsar, Guinea', 'Port Gentil, Gabon', 'Port Harcourt, Nigeria', 'Port Moresby, Papua', 'Port Nador, Morocco', 'Port Neches, Texas,', 'Port Newark, New', 'Port Louis, Mauritius', 'Port Of Spain, Trinidad', 'Port Pirie, Australia', 'Port Raysut, Oman', 'Port Refuge, Cocos', 'Port Royal, Jamaica', 'Port Said, Egypt*', 'Port St. Louis Du Rhone, France', 'Port Sudan, Sudan', 'Malaya, Malaysia', 'Port-Vendres, France', 'Portland, Australia', 'Port Talbot, Wales', 'Portland, England', 'Portland, Oregon, U.S.A.', 'Port Tampa, Florida,', 'Port Taranaki, New', 'Portland, Maine, U.S.A.', 'Porto Alegre, Brazil', 'Porto Di Brindisi, Italy', 'Piombino, Italy', 'Sicily, Italy', 'Portovesme, Italy', 'Porto Grande, Sao', 'Vicente, Cape Verde', 'Portsmouth, England', 'Pozzuoli, Italy', 'Porvoo, Finland', 'Portsmouth, New', 'Hampshire, U.S.A.', 'Poti, Georgia', 'Powell River, Canada', 'Terceira, Azores', 'Praia, Sao Tiago, Cape', 'Preveza, Greece', 'Primorsk, Russia', 'Prince Rupert, Canada', 'Progreso, Mexico', 'Provideniya, Russia', 'Providence, Rhode', 'Island, U.S.A.', 'Puerto De Pasajes, Spain', 'Puerto Manati, Cuba', 'Pulupandan, Philippines', 'Puerto Montt, Chile', 'Puerto Padre, Cuba', 'Puerto Tanamo, Cuba', 'Puerto Vita, Cuba', 'Pula, Croatia', 'Punta Arenas, Chile*', 'Punta Cardon, Venezuela', 'Pusan, South Korea', 'Qabis, Tunisia', 'Puntarenas, Costa Rica', '(Godhavn), Greenland', 'Qingdao, China', 'Qinhuangdao, China', 'Qua Iboe, Nigeria', 'Quepos, Costa Rica', 'Quequen, Argentina', 'Qui Nhon, Vietnam', 'Quinfuguena, Angola', 'Quonset Point, Rhode', 'Rabaul, Papua New', 'Rabigh, Saudi Arabia', 'Rangoon, Burma', 'Rada Di Vado, Italy', 'Randers, Denmark', 'Rapid Bay, Australia', 'Ras Al Kethib, Yemen', 'Ras Al Mishab, Saudi Arabia', 'Ras Al Mishab, Saudi', 'Ras Al Unuf, Libya', 'Ras Silata, Lebanon', 'Rashin, North Korea', 'Rauma, Finland', 'Ravenna, Italy', 'Recife, Brazil', 'Rethimnon, Kriti', 'Reykjavik, Iceland', 'Rhodes, Greece', 'Ribadeo, Spain', 'Richards Bay, South', 'Richmond, California,', 'Riga, Latvia', 'Rijeka, Croatia', 'Rio De Janeiro, Brazil', 'Rio Grande, Brazil', 'Rio Haina, Dominican', 'Risor, Norway', 'Road Harbor, Tortola,', 'Rochefort, France', 'Rochester, England', 'Romana, Dominican Republic', 'Romana, Dominican', 'Rostov-Na-Donu, Russia', 'Ronne, Bornholm,', 'Rosyth, Scotland', 'Rota, Spain', 'Rouen, France', 'Safi, Morocco', 'Rosario, Argentina', 'Rotoava, Iles Tuamotu', 'Roseau, Dominica', 'Rostock, Germany', 'Rumoi, Japan', 'Saida, Lebanon', 'Saipan, Mariana Islands', 'Sabang, Indonesia', 'Sakaide, Japan', 'Sakata, Japan', 'Salamis, Greece', 'Saleef, Yemen', 'Salerno, Italy', 'Salaverry, Peru', 'Salawati, Indonesia', 'Saldanha Bay, South', 'Salina Cruz, Mexico', 'Salinas, Ecuador', 'Salvador, Brazil', 'Sambu, Indonesia', 'Samsun, Turkey', 'San Antonio, Chile', 'San Ciprian, Spain', 'San Diego, California,', 'San Felix, Venezuela', 'San Jose, Guatemala', 'San Juan, Peru', 'San Juan, Puerto Rico', 'San Lorenzo, Argentina', 'San Lorenzo, Honduras', 'Sandakan, Sabah', 'Sandefjorden, Norway', 'San Nicolas, Argentina', 'San Nicolas, Peru', 'San Pedro, Argentina', 'San Pedro, Ivory Coast', 'San Sebastian, Spain', 'San Vicente, Chile', 'San-Men Wen, China', 'San-Ya Chiang, China', 'Sanmen Wen, China', 'Santa Barbara, California, U.S.A.', 'Santa Fe, Argentina', 'Santa Lucia, Cuba', 'Santa Rosalia, Mexico', 'Santa Maria, Cuba', 'Santana, Brazil', 'Santa Marta, Colombia', 'Santiago De Cuba, Cuba', 'Santander, Spain', 'Castilla, Guatemala', 'Santos, Brazil', 'Sao Sebastiao, Brazil', 'Savannah, Georgia, U.S.A.', 'Sanya Gang, China', 'Sao Tome, Sao Tome,', 'Sarande, Albania', 'Sasebo, Japan', 'Savona, Italy', 'Sayda, Lebanon', 'Scapa Flow, Orkney', 'Islands, United Kingdom', 'Searsport, Maine, U.S.A.', 'Seattle, Washington,', 'Selat Sunda, Indonesia*', 'Selat Wetar, Indonesia*', 'Sekondi, Ghana', 'Semarang, Indonesia', 'Sept Iles, Canada', 'Sete, France', 'Setubal, Portugal', 'Severodvinsk, Russia', 'Sevilla, Spain', 'Seward, Alaska, U.S.A.', 'Sfax, Tunisia', 'Shanghai, China', 'Sharjah, United Arab', 'Sharpness, England', 'Sheerness, England', 'Shelburne, Canada', 'Shengjin, Albania', 'Shimizu, Honshu, Japan', 'Shimonoseki, Japan', 'Shimotsui, Japan', 'Shiogama, Japan', 'Sibenik, Croatia', 'Sibu, Malaysia', 'Sidi Ifni, Morocco', 'Simons Bay, South', 'Sines, Portugal', 'Siracusa, Sicily, Italy', 'Sirri Island, Iran', 'Sisimiut, Greenland', 'Sitka, Alaska, U.S.A.', 'Sittwe Harbor, Burma', 'Skagway, Alaska, U.S.A.', 'Skaramangas, Greece', 'Skien, Norway', 'Skikid, Algeria', 'Skredsvik, Sweden', 'Slagen, Norway', 'Slite, Sweden', 'Sonderborg, Denmark', 'Smalkalden, Suriname', 'Sochi, Russia', 'Sorido, Indonesia', 'Sousse, Tunisia', 'Sorong, Indonesia', 'Split, Croatia', 'Soudha, Kriti', 'Sorvagur, Faroe', 'Southampton, England', 'Sriracha, Thailand', 'St. Andrews, Canada', 'St. Georges, Grenada', 'St. Helena Island, South', 'St. John, Canada', 'St. Malo, France', 'St. Marc, Haiti', 'St. Nazaire, France', 'St. Nicholas, Greece', 'St. Petersburg, Florida,', 'St. Pierre, Martinique', 'St. Raphael, France', 'Stadersand, Germany', 'Stenungsund, Sweden', 'Stephenville, Canada', 'Stornoway, Scotland', 'Stockholm, Sweden', 'Sundsvall, Sweden', 'Sunndalsora, Norway', 'Stralsund, Germany', 'Su-Ao Kang, Taiwan', 'Suakin, Sudan', 'Subic Bay, Philippines', 'Sunderland, England', 'Supe Bay, Peru', 'Swan Island, Honduras', 'Surabaya, Indonesia', 'Svendborg, Denmark', 'Suva, Fiji Islands', 'Swansea, Wales', 'Sweeper Cove, Alaska,', 'Swinoujscie, Poland', 'Sydney, Australia', 'Sydney, Canada', 'Szczecin, Poland', 'Tacloban, Philippines', 'Tacoma, Washington,', 'Ta-Ku, China', 'Takoradi, Ghana', 'Tallinn, Estonia', 'Taltal, Chile', 'Taku Bar, China', 'Talara, Peru', 'Tamatave, Madagascar', 'Talcahuano, Chile', 'Tampa, Florida, U.S.A.', 'Tampico, Mexico', 'Tanga, Tanzania', 'Tangier, Morocco', 'Tarabulus, Lebanon', 'Taranto, Italy', 'Tarawa Atoll, Kiribati', 'Tarabulus, Libya', 'Tarbert Island, Ireland', 'Tarragona, Spain', 'Tatibana Ko, Japan', 'Tees River, England', 'Texas City, Texas, U.S.A.', 'Tela, Honduras', 'Thessaloniki, Greece', 'Thames Haven, England', 'Tauranga, New Zealand', 'Tawau, Malaysia', 'Telukbayur, Indonesia', 'Tema, Ghana', 'Thorshavn, Faroe', 'Thule, Greenland', 'Tianjin, China', 'Tonsberg, Norway', 'Tokuyama, Japan', 'Tokyo, Japan', 'Tomakomai, Japan', 'Tornio, Finland', 'Tientsin, China', 'Tiksi, Russia', 'Tjilatjap, Indonesia', 'Tjirebon, Indonesia', 'Tomari, Japan', 'Tompkinsville, New', 'York, U.S.A.', 'Tocopilla, Chile', 'Tongyeong, South', 'Torshavn, Faroe', 'Toulon, France', 'Townsville, Australia', 'Trabzon, Turkey', 'Tramandai, Brazil', 'Trangisvaag, Faroe', 'Trapani, Sicily', 'Travemunde, Germany', 'Trelleborg, Sweden', 'Trenton, New Jersey,', 'Trincomalee, Sri Lanka', 'Trieste, Italy', 'Tromso, Norway', 'Trondheim, Norway', 'Truk, Caroline Islands', 'Tsuruga, Japan', 'Tuapse, Russia', 'Tso-Ying, Taiwan', 'Tumaco, Colombia', 'Tunis, Tunisia', 'Tubruq, Libya', 'Tsingtao, China', 'Tulear, Madagascar', 'Tsugaru-Kaikyo, Japan*', 'Turiamo, Venezuela', 'Turku, Finland', 'Tuticorin, India', 'Tuxpan, Mexico', 'Ube, Japan', 'Uno, Japan', 'Tvedestrand, Norway', 'Ulsan, South Korea', 'Umea, Sweden', 'Valdez, Alaska, U.S.A.', 'Urangan, Australia', 'Umm Said, Qatar', 'Urdiales, Spain', 'Ushant, France*', 'Ushuaia, Argentina', 'Unalakleet, Alaska,', 'Uskudar, Turkey', 'Unggi, North Korea', 'Vadso, Norway', 'Tyne River, England', 'Upernavik, Greenland', 'Uusikaupunki, Finland', 'Vaasa, Finland', 'Valencia, Spain', 'Valparaiso, Chile', 'Valletta, Malta', 'Vancouver, Canada', 'Varberg, Sweden', 'Vardo, Norway', 'Varna, Bulgaria', 'Vejle, Denmark', 'Veraval, India', 'Venice, Italy', 'Ventspils, Latvia', 'Venezia, Italy', 'Victoria, Sabah', 'Veracruz, Mexico', 'Victoria, Seychelles', 'Victoria, Cameroon', 'Vigo, Spain', 'Viareggio, Italy', 'Victoria, Canada', 'Antonio, Portugal', 'Villagarcia, Spain', 'Villefranche, France', 'Vladivostok, Russia', 'Vinh Cam Ranh, Vietnam', 'Villa Do Porto, Azores', 'Vishakhapatnam, India', 'Vita, Cuba', 'Vitoria, Brazil', 'Vlores, Albania', 'Volos, Greece', 'Vung Tau, Vietnam', 'Vyborg, Russia', 'Vysotsk, Russia', 'Wadi Feiran, Egypt', 'Wakamatsu, Japan', 'Wakayama, Japan', 'Wallaroo, Australia', 'Wake Island, Pacific', 'Walvisbaai, Namibia', 'Wakkanai, Japan', 'Wanganui, New Zealand', 'Warnemunde, Germany', 'Warrenpoint, Northern', 'Washington, District', 'Of Columbia, U.S.A.', 'Waterford, Ireland', 'Wei Hai Wei, China', 'Weihai, China', 'Weipa, Australia', 'Wellington, New', 'Wenzhou, China', 'Weonsan, North Korea', 'Whangarei, New', 'Whampoa, China', 'Terminal, Ireland', 'Whitehaven, England', 'Whittier, Alaska, U.S.A.', 'Whyalla, Australia', 'Willemstad, Curacao', 'Wilmington, Delaware,', 'Wilmington, North', 'Wismar, Germany', 'Womens Bay, Alaska,', 'Wonsan, North Korea', 'Wotho, Marshall', 'Wotje Island, Marshall', 'Wrangell, Alaska, U.S.A.', 'Wu-Hu, China', 'Wu-Sung, China', 'Wuhu, China', 'Wusong, China', 'Wyndham, Australia', 'Xiamen, China', 'Yabucoa, Puerto Rico', 'Yandina, Solomon', 'Yakutat, Alaska, U.S.A.', 'Yalta, Russia', 'Yantai, China', 'Yampi Sound, Australia', 'Yanbu Al Bahr, Saudi', 'Yap, Caroline Islands', 'Yarmouth, Canada', 'Yarmouth, England', 'Yen-Tai, China', 'Yeosu, South Korea', 'Yokkaichi, Japan', 'Yokohama, Japan', 'Yokosuka, Japan', 'Yorktown, Virginia,', 'Yosu, South Korea', 'Yumurtalik, Turkey', 'Zadar, Croatia', 'Zanzibar, Tanzania', 'Zamboanga, Philippines', 'Zelinika, Montenegro', 'Zeebrugge, Belgium', 'Zhenjiang, China', 'Zonguldak, Turkey', 'Zueitina, Libya']

def home_screen(surface):
  title_font = pygame.font.SysFont('Josefin Sans', 64)
  arrow_partida = pygame.image.load('assets/arrow.png')
  back_arrow_partida = pygame.image.load('assets/back_arrow.png')

  arrow_destino = pygame.image.load('assets/arrow.png')
  back_arrow_destino = pygame.image.load('assets/back_arrow.png')

  ship = pygame.image.load('assets/ship.png')
  ship = pygame.transform.scale(ship,(358,358))
  arrow_partida = pygame.transform.scale(arrow_partida, (20, 20))
  arrow_destino = pygame.transform.scale(arrow_destino, (20, 20))
  back_arrow_partida = pygame.transform.scale(back_arrow_partida, (20, 20))
  back_arrow_destino = pygame.transform.scale(back_arrow_destino, (20, 20))
  
  title_text = title_font.render('Encontre o melhor roteiro para seu navio', 1, (255, 194, 41))

  surface.blit(back_arrow_partida, (160, 100))
  surface.blit(arrow_partida, (200, 100))
  surface.blit(back_arrow_destino, (880, 100))
  surface.blit(arrow_destino, (920, 100))
  surface.blit(ship, (714, 439))
  surface.blit(title_text, (500, 327))

  pygame.display.update()

def background(surface):
  global search_button
  global button_label
  surface.fill((13, 59, 102))

  label_font = pygame.font.SysFont('Karla', 40)

  btn_img = pygame.image.load('assets/button.png').convert_alpha()
  search_button = button.Button(1400, 90, btn_img, 1)

  partida_index = 12
  destino_index = 263

  label_text = label_font.render(vertices[partida_index], 1, (0, 0, 0))
  label_text2 = label_font.render(vertices[destino_index], 1, (0, 0, 0))
  button_label = label_font.render('Todos a bordo!', 1, (255, 255, 255))

  pygame.draw.rect(surface, (244, 211, 94), (0, 0, 1777, 235))
  
  surface.blit(label_text, (100,60))
  surface.blit(label_text2, (780,60))

  pygame.display.update()


def system():
  background(surface)
  home_screen(surface)
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    surface.blit(button_label, (1460,120))
    pygame.display.update()
  
system()



