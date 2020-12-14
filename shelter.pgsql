--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: pranav
--

COPY public."user" (id, name, surname, email, mobile_number, password) FROM stdin;
1	John	Doe	jd@gmail.com	0000000000	$2b$12$P/boSVRoIaOBFQsMAmmapuICq2scdsF9cLLisBRZMRwqpljTP8/Qy
2	Jane	Parker	jp@gmail.com	1111111111	$2b$12$osVAVqgLH7MYOjH.HWvJVeIyI2BkLUqw8XjjhZJZgnxXD52Qy3QA2
\.


--
-- Data for Name: advertisement; Type: TABLE DATA; Schema: public; Owner: pranav
--

COPY public.advertisement (id, breed_name, location, date_posted, description, image_file, user_id) FROM stdin;
1	Pug	Delhi	2020-12-14 07:43:39.797756	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia explicabo expedita dignissimos delectus, repudiandae eos minima harum atque velit rem quo dolor temporibus, fugit laboriosam exercitationem ad quasi tenetur culpa quisquam fuga! Soluta reiciendis ad repellendus quis necessitatibus possimus officia, excepturi totam libero molestiae, consequatur debitis sint? Earum, quas cum.	9347cdd785f896e6.jpg	1
2	Pariah	Kopargaon	2020-12-14 07:44:14.280474	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia explicabo expedita dignissimos delectus, repudiandae eos minima harum atque velit rem quo dolor temporibus, fugit laboriosam exercitationem ad quasi tenetur culpa quisquam fuga! Soluta reiciendis ad repellendus quis necessitatibus possimus officia, excepturi totam libero molestiae, consequatur debitis sint? Earum, quas cum.	991a3c765f256f5a.jpg	1
3	Spitz	Shirdi	2020-12-14 07:44:40.816404	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia explicabo expedita dignissimos delectus, repudiandae eos minima harum atque velit rem quo dolor temporibus, fugit laboriosam exercitationem ad quasi tenetur culpa quisquam fuga! Soluta reiciendis ad repellendus quis necessitatibus possimus officia, excepturi totam libero molestiae, consequatur debitis sint? Earum, quas cum.	a6f465df7068ece0.jpg	1
4	German Shepherd	Pune	2020-12-14 07:45:17.410817	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia explicabo expedita dignissimos delectus, repudiandae eos minima harum atque velit rem quo dolor temporibus, fugit laboriosam exercitationem ad quasi tenetur culpa quisquam fuga! Soluta reiciendis ad repellendus quis necessitatibus possimus officia, excepturi totam libero molestiae, consequatur debitis sint? Earum, quas cum.	5aa2a1b72039d6e4.jpg	1
5	Siberian Husky	Mumbai	2020-12-14 07:46:24.681487	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia explicabo expedita dignissimos delectus, repudiandae eos minima harum atque velit rem quo dolor temporibus, fugit laboriosam exercitationem ad quasi tenetur culpa quisquam fuga! Soluta reiciendis ad repellendus quis necessitatibus possimus officia, excepturi totam libero molestiae, consequatur debitis sint? Earum, quas cum.	9dd4faeb634e2609.jpg	2
6	Golden Retriever	Panvel	2020-12-14 07:46:58.791931	Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quia explicabo expedita dignissimos delectus, repudiandae eos minima harum atque velit rem quo dolor temporibus, fugit laboriosam exercitationem ad quasi tenetur culpa quisquam fuga! Soluta reiciendis ad repellendus quis necessitatibus possimus officia, excepturi totam libero molestiae, consequatur debitis sint? Earum, quas cum.	9f7831fa53e340a9.jpg	2
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: pranav
--

COPY public.alembic_version (version_num) FROM stdin;
d90a1c3893bd
\.


--
-- Name: advertisement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pranav
--

SELECT pg_catalog.setval('public.advertisement_id_seq', 6, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pranav
--

SELECT pg_catalog.setval('public.user_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

