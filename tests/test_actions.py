"""Tests for the GithubAction and UniqGithubActions classes to ensure correct parsing and comparison."""

from pathlib import Path

from gh_action_pulse.actions import GithubAction, UniqGithubActions


class TestGithubAction:  # pylint: disable=too-few-public-methods
    """Test suite for GithubAction class."""

    # def __init__(self)
    # def __hash__(self)

    def test_github_action__equ__(self) -> None:
        """Test that GithubAction instances are compared correctly (for set usage)."""
        a1 = GithubAction("repo", "v1", "desc")
        a2 = GithubAction("repo", "v1", "desc")
        a3 = GithubAction("repo", "v2", "desc")

        assert a1 == a2
        assert a1 != a3
        assert len({a1, a2}) == 1

    # def get_fully_qualified(self)

    # def _set_recommended_reference_and_date(self, repo: Repository)

    # def _set_actual_description_type(self, repo: Repository)

    # def _set_actual_reference_type_and_date(self, repo: Repository)


class TestUniqGithubActions:  # pylint: disable=too-few-public-methods
    """Test suite for UniqGithubActions class."""

    # def __init__(self) -> None:

    def test_uniq_github_actions_init_from_full_list(self) -> None:
        """Test parsing logic that extracts action name, actual reference, and actual description."""
        path = Path(".github/workflows/myworkflow.yml")
        full_list = {
            path: [{10: "uses: actions/checkout@v4 # pinned to v4"}, {15: "- uses: some-owner/some-repo@master"}]
        }

        uniq = UniqGithubActions()
        uniq.init_from_full_list(full_list)
        actions = list(uniq.get_actions())

        assert len(actions) == 2

        # Sort for deterministic check
        actions.sort(key=lambda x: x.name)

        assert actions[0].name == "actions/checkout"
        assert actions[0].actual.reference == "v4"
        assert actions[0].actual.description == "pinned to v4"

        assert actions[1].name == "some-owner/some-repo"
        assert actions[1].actual.reference == "master"
        assert actions[1].actual.description is None

    # def add(self, action: GithubAction) -> None:

    # def get_actions(self) -> set[GithubAction]

    # def get_fully_qualified(self) -> set[GithubAction]:
