-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2026-01-25 21:49:25 BRT
--   site:      Oracle Database 21c
--   tipo:      Oracle Database 21c


/*
DROP TABLE T_EXE_ALUNO CASCADE CONSTRAINTS 
;

DROP TABLE T_EXE_AULA CASCADE CONSTRAINTS 
;

DROP TABLE T_EXE_CURSO CASCADE CONSTRAINTS 
;

DROP TABLE T_EXE_INSTRUTOR CASCADE CONSTRAINTS 
;

DROP TABLE T_EXE_MATRICULA CASCADE CONSTRAINTS 
;

DROP TABLE T_EXE_PROGRESSO CASCADE CONSTRAINTS 
;
*/

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE T_EXE_ALUNO 
    ( 
     id_aluno    NUMBER (6)  NOT NULL , 
     nm_aluno    VARCHAR2 (60)  NOT NULL , 
     nr_cpf      VARCHAR2 (11)  NOT NULL , 
     ds_email    VARCHAR2 (100)  NOT NULL , 
     nr_telefone NUMBER (11) , 
     dt_cadastro DATE  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_EXE_ALUNO.id_aluno IS 'Identificador único do aluno' 
;

COMMENT ON COLUMN T_EXE_ALUNO.nm_aluno IS 'Nome do aluno - obrigatório' 
;

COMMENT ON COLUMN T_EXE_ALUNO.nr_cpf IS 'Cada aluno deve ter um CPF único. O CPF deve ter exatamente 11 dígitos numéricos ' 
;

COMMENT ON COLUMN T_EXE_ALUNO.ds_email IS 'Endereço de e-mail do aluno. Cada aluno deve ter um e-mail único. O e-mail deve conter ''@'' e pelo menos um ''.''' 
;

COMMENT ON COLUMN T_EXE_ALUNO.nr_telefone IS 'Um aluno pode ter ou não um número de telefone.' 
;

COMMENT ON COLUMN T_EXE_ALUNO.dt_cadastro IS 'Data e hora que o cadastro do aluno foi realizado' 
;

ALTER TABLE T_EXE_ALUNO 
    ADD CONSTRAINT CK_T_EXE_ALUNO_CPF 
    CHECK (REGEXP_LIKE(NR_CPF, '^[0-9]{11}$'))
;


ALTER TABLE T_EXE_ALUNO 
    ADD CONSTRAINT CK_T_EXE_ALUNO_EMAIL 
    CHECK (REGEXP_LIKE(ds_email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'))
;
ALTER TABLE T_EXE_ALUNO 
    ADD CONSTRAINT PK_T_EXE_ALUNO PRIMARY KEY ( id_aluno ) ;

ALTER TABLE T_EXE_ALUNO 
    ADD CONSTRAINT UN_T_EXE_ALUNO_CPF UNIQUE ( nr_cpf ) ;

ALTER TABLE T_EXE_ALUNO 
    ADD CONSTRAINT UN_T_EXE_ALUNO_EMAIL UNIQUE ( ds_email ) ;

CREATE TABLE T_EXE_AULA 
    ( 
     id_aula             NUMBER (10)  NOT NULL , 
     id_curso            NUMBER (5)  NOT NULL , 
     nr_ordem_sequencial NUMBER (3)  NOT NULL , 
     nm_aula             VARCHAR2 (100)  NOT NULL , 
     nr_duracao_minuto   NUMBER (3)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_EXE_AULA.id_aula IS 'Identificador único da aula' 
;

COMMENT ON COLUMN T_EXE_AULA.id_curso IS 'Chave estrangeira - Relacionamento com Curso' 
;

COMMENT ON COLUMN T_EXE_AULA.nr_ordem_sequencial IS 'Número sequencial que ordena as aulas (exemplo: 1,2,3,...n)' 
;

COMMENT ON COLUMN T_EXE_AULA.nm_aula IS 'Nome da aula - obrigatório (exemplo: Aula sobre Relacionamentos em Banco de Dados)' 
;

COMMENT ON COLUMN T_EXE_AULA.nr_duracao_minuto IS 'Duração da aula em minutos' 
;

ALTER TABLE T_EXE_AULA 
    ADD CONSTRAINT CK_T_EXE_AULA_DURACAO 
    CHECK (NR_DURACAO_MINUTO > 0)
;
ALTER TABLE T_EXE_AULA 
    ADD CONSTRAINT PK_T_EXE_AULA PRIMARY KEY ( id_aula ) ;

CREATE TABLE T_EXE_CURSO 
    ( 
     id_curso              NUMBER (5)  NOT NULL , 
     id_instrutor          NUMBER (6)  NOT NULL , 
     nm_curso              VARCHAR2 (100)  NOT NULL , 
     ds_categoria          VARCHAR2 (50)  NOT NULL , 
     vl_preco              NUMBER (8,2)  NOT NULL , 
     dt_cadastro           DATE  NOT NULL , 
     dt_ultima_atualizacao DATE DEFAULT SYSDATE  NOT NULL , 
     st_ativo              CHAR (1)  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_EXE_CURSO.id_curso IS 'Identificador único do curso.' 
;

COMMENT ON COLUMN T_EXE_CURSO.id_instrutor IS 'Cahve estrangeira - Relacionamento com o Instrutor' 
;

COMMENT ON COLUMN T_EXE_CURSO.nm_curso IS 'Nome do curso - obrigatório' 
;

COMMENT ON COLUMN T_EXE_CURSO.ds_categoria IS 'Categoria do curso (exemplo: Programação, Negócios)' 
;

COMMENT ON COLUMN T_EXE_CURSO.vl_preco IS 'Valor Total do Curso' 
;

COMMENT ON COLUMN T_EXE_CURSO.dt_cadastro IS 'Data e hora que o cadastro do curso foi realizado' 
;

COMMENT ON COLUMN T_EXE_CURSO.dt_ultima_atualizacao IS 'Data e hora da ultima alteraçao realizada no cadastro do curso' 
;

COMMENT ON COLUMN T_EXE_CURSO.st_ativo IS 'O status de atividade do curso pode ser: ''S'' (Sim) ou ''N'' (Não) ' 
;

ALTER TABLE T_EXE_CURSO 
    ADD CONSTRAINT CK_T_EXE_CURSO_PRECO 
    CHECK (VL_PRECO > 0)
;


ALTER TABLE T_EXE_CURSO 
    ADD CONSTRAINT CK_T_EXE_CURSO_STATUS 
    CHECK (UPPER(ST_ATIVO) IN ('S', 'N'))
;
ALTER TABLE T_EXE_CURSO 
    ADD CONSTRAINT PK_T_EXE_CURSO PRIMARY KEY ( id_curso ) ;

CREATE TABLE T_EXE_INSTRUTOR 
    ( 
     id_instrutor     NUMBER (6)  NOT NULL , 
     nm_instrutor     VARCHAR2 (60)  NOT NULL , 
     nr_cpf           VARCHAR2 (11)  NOT NULL , 
     ds_especialidade VARCHAR2 (50)  NOT NULL , 
     dt_cadastro      DATE  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_EXE_INSTRUTOR.id_instrutor IS 'Identificador único do instrutor' 
;

COMMENT ON COLUMN T_EXE_INSTRUTOR.nm_instrutor IS 'Nome do instrutor - obrigatório' 
;

COMMENT ON COLUMN T_EXE_INSTRUTOR.nr_cpf IS 'Cada instrutor deve ter um CPF único.
O CPF deve ter exatamente 11 dígitos numéricos.' 
;

COMMENT ON COLUMN T_EXE_INSTRUTOR.ds_especialidade IS 'Especialidade do instrutor (exemplo: Banco de Dados)' 
;

COMMENT ON COLUMN T_EXE_INSTRUTOR.dt_cadastro IS 'Data e hora que o cadastro do instrutor foi realizado' 
;

ALTER TABLE T_EXE_INSTRUTOR 
    ADD CONSTRAINT CK_T_EXE_INSTRUTOR_CPF 
    CHECK (REGEXP_LIKE(NR_CPF, '^[0-9]{11}$'))
;
ALTER TABLE T_EXE_INSTRUTOR 
    ADD CONSTRAINT PK_T_EXE_INSTRUTOR PRIMARY KEY ( id_instrutor ) ;

ALTER TABLE T_EXE_INSTRUTOR 
    ADD CONSTRAINT UN_T_EXE_INSTRUTOR_CPF UNIQUE ( nr_cpf ) ;

CREATE TABLE T_EXE_MATRICULA 
    ( 
     id_matricula       NUMBER (10)  NOT NULL , 
     id_curso           NUMBER (5)  NOT NULL , 
     id_aluno           NUMBER (6)  NOT NULL , 
     dt_matricula       DATE DEFAULT SYSDATE  NOT NULL , 
     vl_pago            NUMBER (8,2)  NOT NULL , 
     ds_forma_pagamento VARCHAR2 (20)  NOT NULL , 
     st_curso           VARCHAR2 (20) DEFAULT 'EM_ANDAMENTO'  NOT NULL , 
     dt_cadastro        DATE  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_EXE_MATRICULA.id_matricula IS 'Identificador único da Matrícula. Cada aluno pode ter uma única matrícula para um determinado curso.' 
;

COMMENT ON COLUMN T_EXE_MATRICULA.id_curso IS 'Compõe o identificador único da tabela Matricula.
Chave estrangeira - Relacionamento com Curso' 
;

COMMENT ON COLUMN T_EXE_MATRICULA.id_aluno IS 'Chave estrangeira - Relacionamento com Aluno' 
;

COMMENT ON COLUMN T_EXE_MATRICULA.dt_matricula IS 'A data de matrícula deve ser preenchida automaticamente com a data atual ' 
;

COMMENT ON COLUMN T_EXE_MATRICULA.vl_pago IS 'Valor pago pelo curso' 
;

COMMENT ON COLUMN T_EXE_MATRICULA.ds_forma_pagamento IS 'A forma de pagamento pode ser: ''Cartão de Crédito'', ''PIX'', ''Boleto''' 
;

COMMENT ON COLUMN T_EXE_MATRICULA.st_curso IS 'O status de um curso deve ser ''EM_ANDAMENTO'' por padrão.
O status de um curso pode ser: ''EM_ANDAMENTO'', ''CONCLUIDO'' ou ''CANCELADO'' ' 
;

COMMENT ON COLUMN T_EXE_MATRICULA.dt_cadastro IS 'Data e hora que o cadastro da matricula foi realizado' 
;

ALTER TABLE T_EXE_MATRICULA 
    ADD CONSTRAINT CK_T_EXE_MATRICULA_VLPAGO 
    CHECK (VL_PAGO >= 0)
;


ALTER TABLE T_EXE_MATRICULA 
    ADD CONSTRAINT CK_T_EXE_MATRICULA_STATUS 
    CHECK (UPPER(ST_CURSO) IN ('EM_ANDAMENTO', 'CONCLUIDO', 'CANCELADO'))
;


ALTER TABLE T_EXE_MATRICULA 
    ADD CONSTRAINT CK_T_EXE_MATRICULA_FORMA 
    CHECK (UPPER(DS_FORMA_PAGAMENTO) IN ('CARTÃO DE CRÉDITO', 'PIX', 'BOLETO'))
;
ALTER TABLE T_EXE_MATRICULA 
    ADD CONSTRAINT PK_T_EXE_MATRICULA PRIMARY KEY ( id_matricula ) ;

ALTER TABLE T_EXE_MATRICULA 
    ADD CONSTRAINT UN_T_EXE_MATRICULA_CURSO UNIQUE ( id_matricula , id_curso ) ;

CREATE TABLE T_EXE_PROGRESSO 
    ( 
     id_matricula          NUMBER (10)  NOT NULL , 
     id_aula               NUMBER (10)  NOT NULL , 
     dt_aula_assistida     DATE  NOT NULL , 
     st_concluida          CHAR (1) DEFAULT 'N'  NOT NULL , 
     dt_ultima_atualizacao DATE DEFAULT SYSDATE  NOT NULL 
    ) 
;

COMMENT ON COLUMN T_EXE_PROGRESSO.id_matricula IS 'Compõe o identificador único da tabela Progresso.
Chave estrangeira - Relacionamento com Matricula.
' 
;

COMMENT ON COLUMN T_EXE_PROGRESSO.id_aula IS 'Compõe o identificador único da tabela Progresso.
Chave estrangeira - Relacionamento com Aula.
' 
;

COMMENT ON COLUMN T_EXE_PROGRESSO.dt_aula_assistida IS 'Data em que a aula foi assistida' 
;

COMMENT ON COLUMN T_EXE_PROGRESSO.st_concluida IS 'O status de conclusão de uma aula deve ser ''N'' por padrão.
O status de conclusão de uma aula pode ser: ''S'' (Sim) ou ''N'' (Não) ' 
;

COMMENT ON COLUMN T_EXE_PROGRESSO.dt_ultima_atualizacao IS 'Data e hora da ultima alteraçao realizada no progesso do aluno.' 
;

ALTER TABLE T_EXE_PROGRESSO 
    ADD CONSTRAINT CK_T_EXE_PROGRESSO_STATUS 
    CHECK (UPPER(ST_CONCLUIDA) IN ('S', 'N'))
;
ALTER TABLE T_EXE_PROGRESSO 
    ADD CONSTRAINT PK_T_EXE_PROGRESSO PRIMARY KEY ( id_matricula, id_aula ) ;

ALTER TABLE T_EXE_AULA 
    ADD CONSTRAINT FK_T_EXE_AULA_CURSO FOREIGN KEY 
    ( 
     id_curso
    ) 
    REFERENCES T_EXE_CURSO 
    ( 
     id_curso
    ) 
;

ALTER TABLE T_EXE_CURSO 
    ADD CONSTRAINT FK_T_EXE_CURSO_INSTRUTOR FOREIGN KEY 
    ( 
     id_instrutor
    ) 
    REFERENCES T_EXE_INSTRUTOR 
    ( 
     id_instrutor
    ) 
;

ALTER TABLE T_EXE_MATRICULA 
    ADD CONSTRAINT FK_T_EXE_MATRICULA_ALUNO FOREIGN KEY 
    ( 
     id_aluno
    ) 
    REFERENCES T_EXE_ALUNO 
    ( 
     id_aluno
    ) 
;

ALTER TABLE T_EXE_MATRICULA 
    ADD CONSTRAINT FK_T_EXE_MATRICULA_CURSO FOREIGN KEY 
    ( 
     id_curso
    ) 
    REFERENCES T_EXE_CURSO 
    ( 
     id_curso
    ) 
;

ALTER TABLE T_EXE_PROGRESSO 
    ADD CONSTRAINT FK_T_EXE_PROGRESSO_AULA FOREIGN KEY 
    ( 
     id_aula
    ) 
    REFERENCES T_EXE_AULA 
    ( 
     id_aula
    ) 
;

ALTER TABLE T_EXE_PROGRESSO 
    ADD CONSTRAINT FK_T_EXE_PROGRESSO_MATRICULA FOREIGN KEY 
    ( 
     id_matricula
    ) 
    REFERENCES T_EXE_MATRICULA 
    ( 
     id_matricula
    ) 
;


-- Exemplo de uso de GENERATED AS IDENTITY na tabela ALUNO
/*
CREATE TABLE T_EXE_ALUNO 
    ( 
     id_aluno    NUMBER (6) GENERATED ALWAYS AS IDENTITY, 
     nm_aluno    VARCHAR2 (60)  NOT NULL , 
     nr_cpf      VARCHAR2 (11)  NOT NULL , 
     ds_email    VARCHAR2 (100)  NOT NULL , 
     nr_telefone NUMBER (11) , 
     dt_cadastro DATE  NOT NULL 
    ) 
;
*/


-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             26
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
