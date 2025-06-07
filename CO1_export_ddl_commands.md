# CO1 Export DDL Commands

```bash
expdp your_user/your_pass@APP1DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP1_APP1DB1_SCHEMA1_ddl.dmp \
  LOGFILE=CO1_APP1_APP1DB1_SCHEMA1_ddl.log \
  SCHEMAS=SCHEMA1 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP1DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP1_APP1DB1_SCHEMA1_ddl.dmp \
  SQLFILE=CO1_APP1_APP1DB1_SCHEMA1_schema_ddl.sql \
  SCHEMAS=SCHEMA1 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP1DB2 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP1_APP1DB2_SCHEMA2_ddl.dmp \
  LOGFILE=CO1_APP1_APP1DB2_SCHEMA2_ddl.log \
  SCHEMAS=SCHEMA2 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP1DB2 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP1_APP1DB2_SCHEMA2_ddl.dmp \
  SQLFILE=CO1_APP1_APP1DB2_SCHEMA2_schema_ddl.sql \
  SCHEMAS=SCHEMA2 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP2DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP2_APP2DB1_SCHEMA3_ddl.dmp \
  LOGFILE=CO1_APP2_APP2DB1_SCHEMA3_ddl.log \
  SCHEMAS=SCHEMA3 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP2DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP2_APP2DB1_SCHEMA3_ddl.dmp \
  SQLFILE=CO1_APP2_APP2DB1_SCHEMA3_schema_ddl.sql \
  SCHEMAS=SCHEMA3 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP3DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP3_APP3DB1_SCHEMA4_ddl.dmp \
  LOGFILE=CO1_APP3_APP3DB1_SCHEMA4_ddl.log \
  SCHEMAS=SCHEMA4 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP3DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP3_APP3DB1_SCHEMA4_ddl.dmp \
  SQLFILE=CO1_APP3_APP3DB1_SCHEMA4_schema_ddl.sql \
  SCHEMAS=SCHEMA4 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP4DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP4_APP4DB1_SCHEMA5_ddl.dmp \
  LOGFILE=CO1_APP4_APP4DB1_SCHEMA5_ddl.log \
  SCHEMAS=SCHEMA5 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP4DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP4_APP4DB1_SCHEMA5_ddl.dmp \
  SQLFILE=CO1_APP4_APP4DB1_SCHEMA5_schema_ddl.sql \
  SCHEMAS=SCHEMA5 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP5DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP5_APP5DB1_SCHEMA6_ddl.dmp \
  LOGFILE=CO1_APP5_APP5DB1_SCHEMA6_ddl.log \
  SCHEMAS=SCHEMA6 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP5DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP5_APP5DB1_SCHEMA6_ddl.dmp \
  SQLFILE=CO1_APP5_APP5DB1_SCHEMA6_schema_ddl.sql \
  SCHEMAS=SCHEMA6 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP6DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP6_APP6DB1_SCHEMA7_ddl.dmp \
  LOGFILE=CO1_APP6_APP6DB1_SCHEMA7_ddl.log \
  SCHEMAS=SCHEMA7 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP6DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP6_APP6DB1_SCHEMA7_ddl.dmp \
  SQLFILE=CO1_APP6_APP6DB1_SCHEMA7_schema_ddl.sql \
  SCHEMAS=SCHEMA7 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP7DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP7_APP7DB1_SCHEMA8_ddl.dmp \
  LOGFILE=CO1_APP7_APP7DB1_SCHEMA8_ddl.log \
  SCHEMAS=SCHEMA8 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP7DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP7_APP7DB1_SCHEMA8_ddl.dmp \
  SQLFILE=CO1_APP7_APP7DB1_SCHEMA8_schema_ddl.sql \
  SCHEMAS=SCHEMA8 \
  CONTENT=METADATA_ONLY
```

```bash
expdp your_user/your_pass@APP8DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP8_APP8DB1_SCHEMA9_ddl.dmp \
  LOGFILE=CO1_APP8_APP8DB1_SCHEMA9_ddl.log \
  SCHEMAS=SCHEMA9 \
  CONTENT=METADATA_ONLY
```

```bash
impdp your_user/your_pass@APP8DB1 \
  DIRECTORY=dpump_dir \
  DUMPFILE=CO1_APP8_APP8DB1_SCHEMA9_ddl.dmp \
  SQLFILE=CO1_APP8_APP8DB1_SCHEMA9_schema_ddl.sql \
  SCHEMAS=SCHEMA9 \
  CONTENT=METADATA_ONLY
```
