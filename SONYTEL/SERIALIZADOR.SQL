/*
Created: 15/06/2015
Modified: 24/07/2015
Model: Sonitel.db
Database: PostgreSQL 9.2
*/

-- Create tables section -------------------------------------------------

-- Table CLIENTES

CREATE TABLE "CLIENTES"(
 "cli_cedula" Character varying(10) NOT NULL,
 "cli_nombre" Character varying(30) NOT NULL,
 "cli_apellido" Character varying(30) NOT NULL,
 "cli_telefono" Character varying(10),
 "cli_direccion" Character varying(75) NOT NULL,
 "cli_email" Character varying(75) NOT NULL,
 "cli_estado" Character varying(1) NOT NULL,
 "ciu_id" Integer,
 "cli_id" Serial NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table CLIENTES

ALTER TABLE "CLIENTES" ADD CONSTRAINT "Key1" PRIMARY KEY ("cli_id")
;

-- Table PROVEEDOR

CREATE TABLE "PROVEEDOR"(
 "prov_id" Serial NOT NULL,
 "prov_ruc" Character varying(10) NOT NULL,
 "prov_cedula" Character varying(10) NOT NULL,
 "prov_nombre" Character varying(30) NOT NULL,
 "prov_representante" Character varying(50) NOT NULL,
 "prov_direccion" Character varying(80) NOT NULL,
 "prov_telefono" Character varying(10),
 "ciu_id" Integer,
 "prov_estado" Character varying(1)
)
WITH (OIDS=FALSE)
;

-- Add keys for table PROVEEDOR

ALTER TABLE "PROVEEDOR" ADD CONSTRAINT "Key4" PRIMARY KEY ("prov_id")
;

-- Table CIUDAD

CREATE TABLE "CIUDAD"(
 "ciu_id" Serial NOT NULL,
 "ciu_nombre" Character varying(30) NOT NULL,
 "ciu_descripcion" Character varying(70) NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table CIUDAD

ALTER TABLE "CIUDAD" ADD CONSTRAINT "Key5" PRIMARY KEY ("ciu_id")
;

-- Table FACTURADETALLE

CREATE TABLE "FACTURADETALLE"(
 "fac_id" Integer,
 "pro_id" Integer,
 "det_cantiadd" Integer NOT NULL,
 "det_preciou" Double precision NOT NULL,
 "det_preciot" Double precision NOT NULL
)
WITH (OIDS=FALSE)
;

-- Table FACTURA

CREATE TABLE "FACTURA"(
 "fac_id" Serial NOT NULL,
 "fac_subtotal" Double precision NOT NULL,
 "fac_iva" Double precision NOT NULL,
 "fac_descuento" Double precision NOT NULL,
 "fac_total" Double precision NOT NULL,
 "fac_fecha" Date NOT NULL,
 "fac_estado" Character varying(1) NOT NULL,
 "cli_id" Integer
)
WITH (OIDS=FALSE)
;

-- Add keys for table FACTURA

ALTER TABLE "FACTURA" ADD CONSTRAINT "Key7" PRIMARY KEY ("fac_id")
;

-- Table PRODUCTOS

CREATE TABLE "PRODUCTOS"(
 "pro_id" Serial NOT NULL,
 "pro_nombre" Character varying(30) NOT NULL,
 "pro_cantidad" Integer NOT NULL,
 "pro_precio" Double precision NOT NULL,
 "pro_ecg" Character varying(75),
 "pro_tarifa_iva" Double precision NOT NULL,
 "pro_ex" Integer NOT NULL,
 "pro_pvp" Double precision NOT NULL,
 "mar_id" Integer
)
WITH (OIDS=FALSE)
;

-- Add keys for table PRODUCTOS

ALTER TABLE "PRODUCTOS" ADD CONSTRAINT "Key8" PRIMARY KEY ("pro_id")
;

-- Table ARTICULOSSEGUNDA

CREATE TABLE "ARTICULOSSEGUNDA"(
 "art_id" Serial NOT NULL,
 "art_nombre" Character varying(30) NOT NULL,
 "art_precio" Double precision NOT NULL,
 "art_cantidad" Integer NOT NULL,
 "art_serie" Character varying(50) NOT NULL,
 "mar_id" Integer,
 "mod_id" Integer,
 "art_estado" Character varying(1) NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table ARTICULOSSEGUNDA

ALTER TABLE "ARTICULOSSEGUNDA" ADD CONSTRAINT "Key9" PRIMARY KEY ("art_id")
;

-- Table CATEGORIA

CREATE TABLE "CATEGORIA"(
 "mar_id" Serial NOT NULL,
 "mar_nombre" Character varying(30) NOT NULL,
 "mar_descripcion" Character varying(75) NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table CATEGORIA

ALTER TABLE "CATEGORIA" ADD CONSTRAINT "Key11" PRIMARY KEY ("mar_id")
;

-- Table MODELO

CREATE TABLE "MODELO"(
 "mod_id" Serial NOT NULL,
 "mod_nombre" Character varying(30) NOT NULL,
 "mod_descripcion" Character varying(75) NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table MODELO

ALTER TABLE "MODELO" ADD CONSTRAINT "Key12" PRIMARY KEY ("mod_id")
;

-- Table SOLICITUDMANTENIMIENTO

CREATE TABLE "SOLICITUDMANTENIMIENTO"(
 "solm_id" Serial NOT NULL,
 "solm_fecha" Date NOT NULL,
 "solm_falla" Character varying(100) NOT NULL,
 "solm_observaciones" Character varying(100),
 "solm_abono" Double precision NOT NULL,
 "solm_saldo" Double precision NOT NULL,
 "solm_total" Double precision NOT NULL,
 "solm_estado" Character varying(1),
 "art_id" Integer NOT NULL,
 "cli_id" Integer
)
WITH (OIDS=FALSE)
;

-- Add keys for table SOLICITUDMANTENIMIENTO

ALTER TABLE "SOLICITUDMANTENIMIENTO" ADD CONSTRAINT "Key13" PRIMARY KEY ("solm_id")
;

-- Table MANTENIMIENTO

CREATE TABLE "MANTENIMIENTO"(
 "man_id" Serial NOT NULL,
 "man_fecha" Date NOT NULL,
 "man_garantia" Integer NOT NULL,
 "man_informe" Character varying(300) NOT NULL,
 "man_fechaentrega" Date NOT NULL,
 "man_estado" Character varying(1),
 "solm_id" Integer NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table MANTENIMIENTO

ALTER TABLE "MANTENIMIENTO" ADD CONSTRAINT "Key14" PRIMARY KEY ("man_id")
;

-- Table REPUESTOS

CREATE TABLE "REPUESTOS"(
 "man_id" Integer NOT NULL,
 "pro_id" Integer NOT NULL,
 "rep_cantidad" Integer NOT NULL
)
WITH (OIDS=FALSE)
;

-- Table DETALLEPROVEEDOR

CREATE TABLE "DETALLEPROVEEDOR"(
 "pro_id" Integer NOT NULL,
 "kar_Precio_proveedor" Double precision NOT NULL,
 "kar_entra" Integer NOT NULL,
 "kar_sald" Integer NOT NULL,
 "kar_fecha" Timestamp with time zone NOT NULL,
 "ord_id" Integer
)
WITH (OIDS=FALSE)
;

-- Add keys for table DETALLEPROVEEDOR

ALTER TABLE "DETALLEPROVEEDOR" ADD CONSTRAINT "Key16" PRIMARY KEY ("pro_id")
;

-- Table FACTURADETALLEMANTENIMIENTO

CREATE TABLE "FACTURADETALLEMANTENIMIENTO"(
 "fac_id" Integer NOT NULL,
 "solm_id" Integer NOT NULL,
 "fad_preciou" Double precision NOT NULL,
 "fad_preciot" Double precision NOT NULL
)
WITH (OIDS=FALSE)
;

-- Table ORDEN DE COMPRA

CREATE TABLE "ORDEN DE COMPRA"(
 "ord_id" Serial NOT NULL,
 "ord_subtotal" Double precision NOT NULL,
 "ord_iva" Double precision NOT NULL,
 "ord_descuento" Double precision NOT NULL,
 "ord_total" Double precision NOT NULL,
 "ord_fecha" Date NOT NULL,
 "prov_id" Integer NOT NULL,
 "ord_estado" Character varying(1) NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table ORDEN DE COMPRA

ALTER TABLE "ORDEN DE COMPRA" ADD CONSTRAINT "Key20" PRIMARY KEY ("ord_id")
;

-- Table MENSAJERIA

CREATE TABLE "MENSAJERIA"(
 "men_id" Serial NOT NULL,
 "men_asunto" Character varying(30) NOT NULL,
 "men_descripcion" Character varying(500) NOT NULL,
 "cli_id" Integer NOT NULL
)
WITH (OIDS=FALSE)
;

-- Add keys for table MENSAJERIA

ALTER TABLE "MENSAJERIA" ADD CONSTRAINT "Key21" PRIMARY KEY ("men_id","cli_id")
;

-- Create relationships section ------------------------------------------------- 

ALTER TABLE "PROVEEDOR" ADD CONSTRAINT "Relationship1" FOREIGN KEY ("ciu_id") REFERENCES "CIUDAD" ("ciu_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "CLIENTES" ADD CONSTRAINT "Relationship2" FOREIGN KEY ("ciu_id") REFERENCES "CIUDAD" ("ciu_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "ARTICULOSSEGUNDA" ADD CONSTRAINT "Relationship5" FOREIGN KEY ("mar_id") REFERENCES "CATEGORIA" ("mar_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "ARTICULOSSEGUNDA" ADD CONSTRAINT "Relationship6" FOREIGN KEY ("mod_id") REFERENCES "MODELO" ("mod_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "FACTURADETALLE" ADD CONSTRAINT "Relationship10" FOREIGN KEY ("fac_id") REFERENCES "FACTURA" ("fac_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "FACTURADETALLE" ADD CONSTRAINT "Relationship11" FOREIGN KEY ("pro_id") REFERENCES "PRODUCTOS" ("pro_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "SOLICITUDMANTENIMIENTO" ADD CONSTRAINT "Relationship13" FOREIGN KEY ("art_id") REFERENCES "ARTICULOSSEGUNDA" ("art_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "SOLICITUDMANTENIMIENTO" ADD CONSTRAINT "Relationship14" FOREIGN KEY ("cli_id") REFERENCES "CLIENTES" ("cli_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "MANTENIMIENTO" ADD CONSTRAINT "Relationship19" FOREIGN KEY ("solm_id") REFERENCES "SOLICITUDMANTENIMIENTO" ("solm_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "REPUESTOS" ADD CONSTRAINT "Relationship20" FOREIGN KEY ("man_id") REFERENCES "MANTENIMIENTO" ("man_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "REPUESTOS" ADD CONSTRAINT "Relationship21" FOREIGN KEY ("pro_id") REFERENCES "PRODUCTOS" ("pro_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "DETALLEPROVEEDOR" ADD CONSTRAINT "Relationship25" FOREIGN KEY ("pro_id") REFERENCES "PRODUCTOS" ("pro_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "FACTURADETALLEMANTENIMIENTO" ADD CONSTRAINT "Relationship28" FOREIGN KEY ("fac_id") REFERENCES "FACTURA" ("fac_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "FACTURADETALLEMANTENIMIENTO" ADD CONSTRAINT "Relationship29" FOREIGN KEY ("solm_id") REFERENCES "SOLICITUDMANTENIMIENTO" ("solm_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "ORDEN DE COMPRA" ADD CONSTRAINT "Relationship30" FOREIGN KEY ("prov_id") REFERENCES "PROVEEDOR" ("prov_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "DETALLEPROVEEDOR" ADD CONSTRAINT "Relationship31" FOREIGN KEY ("ord_id") REFERENCES "ORDEN DE COMPRA" ("ord_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "PRODUCTOS" ADD CONSTRAINT "Relationship32" FOREIGN KEY ("mar_id") REFERENCES "CATEGORIA" ("mar_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "MENSAJERIA" ADD CONSTRAINT "Relationship33" FOREIGN KEY ("cli_id") REFERENCES "CLIENTES" ("cli_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "FACTURA" ADD CONSTRAINT "Relationship34" FOREIGN KEY ("cli_id") REFERENCES "CLIENTES" ("cli_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;





