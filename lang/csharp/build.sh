#!/bin/bash

set -e 
dotnet --info
dotnet restore

dotnet build --framework netcoreapp2.0 --configuration Release ./src/apache/codegen/Avro.codegen.csproj
dotnet build --framework netstandard2.0 --configuration Release ./src/apache/main/Avro.main.csproj
dotnet build --framework netstandard2.0 --configuration Release ./src/apache/msbuild/Avro.msbuild.csproj
dotnet test --framework netcoreapp2.0 --configuration Release ./src/apache/test/Avro.test.csproj
