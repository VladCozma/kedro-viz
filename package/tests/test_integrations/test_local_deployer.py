from kedro_viz import __version__
from kedro_viz.integrations.deployment.local_deployer import LocalDeployer


# Test the LocalDeployer class
class TestLocalDeployer:
    def test_deploy(self, mocker):
        mocker.patch("fsspec.filesystem")
        deployer = LocalDeployer()

        mocker.patch.object(deployer, "_upload_api_responses")
        mocker.patch.object(deployer, "_upload_static_files")
        mocker.patch.object(deployer, "_upload_deploy_viz_metadata_file")

        deployer.deploy()

        deployer._upload_api_responses.assert_called_once()
        deployer._upload_static_files.assert_called_once()
        deployer._upload_deploy_viz_metadata_file.assert_called_once()
