--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: brands_makers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.brands_makers (
    brands integer NOT NULL,
    makers integer NOT NULL
);


ALTER TABLE public.brands_makers OWNER TO postgres;

--
-- Name: car_brands; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car_brands (
    id integer NOT NULL,
    brand_name character varying(100) NOT NULL
);


ALTER TABLE public.car_brands OWNER TO postgres;

--
-- Name: car_makers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car_makers (
    id integer NOT NULL,
    maker_name character varying(100) NOT NULL
);


ALTER TABLE public.car_makers OWNER TO postgres;

--
-- Name: car_models; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.car_models (
    id integer NOT NULL,
    model_name character varying(50) NOT NULL,
    model_id integer NOT NULL
);


ALTER TABLE public.car_models OWNER TO postgres;

--
-- Name: makers_models; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.makers_models (
    makers_id integer NOT NULL,
    models_id integer NOT NULL
);


ALTER TABLE public.makers_models OWNER TO postgres;

--
-- Name: models_brands; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.models_brands (
    models integer NOT NULL,
    brands integer NOT NULL
);


ALTER TABLE public.models_brands OWNER TO postgres;

--
-- Data for Name: brands_makers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.brands_makers (brands, makers) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
\.


--
-- Data for Name: car_brands; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.car_brands (id, brand_name) FROM stdin;
1	Alfa Romeo
2	Dodge
3	Mazda
4	Nissan
5	Tesla
6	Volkswagen
\.


--
-- Data for Name: car_makers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.car_makers (id, maker_name) FROM stdin;
1	Alfa Romeo Automobiles S.p.A.
2	Chrysler
3	Mazda Motor Corporation
4	Nissan Motor Company
5	Tesla
6	Volkswagen AG
7	Volvo Cars
\.


--
-- Data for Name: car_models; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.car_models (id, model_name, model_id) FROM stdin;
1	Alfa Romeo Stelvio	1
2	Dodge Journey	2
3	Mazda Axela	3
4	Nissan LEAF	4
5	Tesla Model S	5
6	Tesla Model 3	5
\.


--
-- Data for Name: makers_models; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.makers_models (makers_id, models_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
5	6
\.


--
-- Data for Name: models_brands; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.models_brands (models, brands) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	5
\.


--
-- PostgreSQL database dump complete
--

