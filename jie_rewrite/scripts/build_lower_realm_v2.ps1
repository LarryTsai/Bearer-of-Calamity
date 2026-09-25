# Compatibility entry point for the current outline-based publication workflow.
param([switch]$Check, [switch]$AllowLegacy)
$taskBuildArgs = @((Join-Path $PSScriptRoot 'build_story.py'))
if ($Check) { $taskBuildArgs += '--check' }
if ($AllowLegacy) { $taskBuildArgs += '--allow-legacy' }
& python @taskBuildArgs
exit $LASTEXITCODE
