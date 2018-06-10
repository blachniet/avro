param(
	[Parameter(Position=0)]
	[ValidateSet("Default")]
	[string]
	$Target = "Default",

	[Parameter()]
	[ValidateSet("Release","Debug")]
	[string]
	$Configuration = "Release"
)

$ErrorActionPreference = 'Stop'
trap {
	$ErrorActionPreference = 'Continue'
	Write-Error $_
	exit 1
}

function CheckExitCode {
	if ($LASTEXITCODE) {
		exit $LASTEXITCODE
	}
}

function Clean {
	Get-ChildItem ".\src\apache\*\bin" | Remove-Item -Recurse -Force
	Get-ChildItem ".\src\apache\*\obj" | Remove-Item -Recurse -Force
}

function Build {
	Clean

	& dotnet build --configuration $Configuration
	CheckExitCode
}

function Test {
	Build

	Get-ChildItem ".\src\apache\*test" | Foreach-Object {
		Push-Location $_.FullName
		& dotnet test --configuration $Configuration
		Pop-Location
		CheckExitCode
	}
}

function Default {
	Test
}

Push-Location $PSScriptRoot
try {
	Invoke-Expression $Target
} finally {
	Pop-Location
}
