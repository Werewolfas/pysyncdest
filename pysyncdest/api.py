import urllib
import requests

import pysyncdest

DESTINY2_URL = 'https://www.bungie.net/Platform/Destiny2/'
USER_URL = 'https://www.bungie.net/Platform/User/'
GROUP_URL = 'https://www.bungie.net/Platform/GroupV2/'


class API:
    """This module contains requests for the Destiny 2 API.
    There is some documentation provided here as to how to use
    these functions, but you will likely need to refer to the
    official API documentation as well. The documentation can be
    found at https://bungie-net.github.io/multi/index.html
    """

    def __init__(self, api_key):
        self.api_key = api_key

    def _get_request(self, url):
        """Make an async GET request and attempt to return json (dict)"""
        headers = {'X-API-KEY': '{}'.format(self.api_key)}
        encoded_url = urllib.parse.quote(url, safe=':/?&=,.')
        try:
            json_res = requests.get(encoded_url, headers=headers).json()
        except (requests.ConnectionError, requests.ConnectTimeout) as e:
            raise pysyncdest.PysyncdestException("Could not connect to Bungie.net")
        return json_res

    def get_bungie_net_user_by_id(self, bungie_id):
        """Loads a bungienet user by membership id
        Args:
            bungie_id: The requested Bungie.net membership id
        Returns:
            json (dict)
        """
        url = USER_URL + 'GetBungieNetUserById/{}/'
        url = url.format(bungie_id)
        return self._get_request(url)

    def get_membership_data_by_id(self, bungie_id, membership_type=-1):
        """Returns a list of accounts associated with the supplied membership ID and membership
        type. This will include all linked accounts (even when hidden) if supplied credentials
        permit it.
        Args:
            bungie_id:
                The requested Bungie.net membership id
            membership_type (optional):
                Type of the supplied membership ID. If not provided, data will be returned for all
                applicable platforms.
        Returns:
            json (dict)
        """
        url = USER_URL + 'GetMembershipsById/{}/{}/'
        url = url.format(bungie_id, membership_type)
        return self._get_request(url)

    def get_destiny_manifest(self):
        """Returns the current version of the manifest
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'Manifest'
        return self._get_request(url)

    def search_destiny_entities(self, entity_type, search_term, page=0):
        """Gets a page list of Destiny items
        Args:
            entity_type:
                The type of entity - ex. 'DestinyInventoryItemDefinition'
            search_term:
                The full gamertag or PSN id of the player. Spaces and case are ignored
            page (optional):
                Page number to return
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'Armory/Search/{}/{}/?page={}'
        url = url.format(entity_type, search_term, page)
        return self._get_request(url)

    def search_destiny_player(self, membership_type, display_name):
        """Returns a list of Destiny memberships given a full Gamertag or PSN ID
        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            display_name (str):
                The full gamertag or PSN id of the player. Spaces and case are ignored.
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'SearchDestinyPlayer/{}/{}/'
        url = url.format(membership_type, display_name)
        return self._get_request(url)

    def get_profile(self, membership_type, membership_id, components):
        """Returns Destiny Profile information for the supplied membership
        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID
            components (list):
                A list containing the components  to include in the response.
                (see Destiny.Responses.DestinyProfileResponse). At least one
                component is required to receive results. Can use either ints
                or strings.
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + '{}/Profile/{}/?components={}'
        url = url.format(membership_type, membership_id, ','.join([str(i) for i in components]))
        return self._get_request(url)

    def get_character(self, membership_type, membership_id, character_id, components):
        """Returns character information for the supplied character
        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID
            character_id (int):
                ID of the character
            components (list):
                A list containing the components  to include in the response.
                (see Destiny.Responses.DestinyProfileResponse). At least one
                component is required to receive results. Can use either ints
                or strings.
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + '{}/Profile/{}/Character/{}/?components={}'
        url = url.format(membership_type, membership_id, character_id, ','.join([str(i) for i in components]))
        return self._get_request(url)

    def get_clan_weekly_reward_state(self, group_id):
        """Returns information on the weekly clan rewards and if the clan has earned
        them or not. Note that this will always report rewards as not redeemed.
        Args:
            group_id (int):
                A valid group ID of a clan
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'Clan/{}/WeeklyRewardState/'
        url = url.format(group_id)
        return self._get_request(url)

    def get_item(self, membership_type, membership_id, item_instance_id, components):
        """Retrieve the details of an instanced Destiny Item. An instanced Destiny
        item is one with an ItemInstanceId. Non-instanced items, such as materials,
        have no useful instance-specific details and thus are not queryable here.
        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID
            item_instance_id (int):
                The instance ID of the item
            components (list):
                A list containing the components to include in the response
                (see Destiny.Responses.DestinyItemResponse). At least one
                component is required to receive results. Can use either ints
                or strings.
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + '{}/Profile/{}/Item/{}/?components={}'
        url = url.format(membership_type, membership_id, item_instance_id, ','.join([str(i) for i in components]))
        return self._get_request(url)

    def get_post_game_carnage_report(self, activity_id):
        """Gets the available post game carnage report for the activity ID
        Args:
            activity_id (int):
                The ID of the activity whose PGCR is requested
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'Stats/PostGameCarnageReport/{}/'
        url = url.format(activity_id)
        return self._get_request(url)

    def get_historical_stats_definition(self):
        """Gets historical stats definitions
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'Stats/Definition/'
        return self._get_request(url)

    def get_historical_stats(self, membership_type, membership_id, character_id=0, groups=[], modes=[]):
        """Gets historical stats for indicated character
        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID
            character_id (int) [optional]:
                The id of the character to retrieve stats for. If not provided, stats for all
                characters will be retrieved.
            groups (list - str/int):
                A list containing the groups of stats to include in the response
                (see Destiny.HistoricalStats.Definitions.DestinyStatsGroupType).
            modes (list - str/int):
                A list containing the game modes to include in the response
                (see Destiny.HistoricalStats.Definitions.DestinyActivityModeType).
        """
        url = DESTINY2_URL + '{}/Account/{}/Character/{}/Stats/?groups={}&modes={}'
        url = url.format(membership_type, membership_id, character_id, ','.join([str(i) for i in groups]),
                         ','.join([str(i) for i in modes]))
        return self._get_request(url)

    def get_public_milestone_content(self, milestone_hash):
        """Gets custom localized content for the milestone of
        the given hash, if it exists.

        Args:
            milestone_hash (int):
                A valid hash id of a Destiny 2 milestone

        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'Milestones/{}/Content/'
        url = url.format(milestone_hash)
        return self._get_request(url)

    def get_public_milestones(self):
        """Gets information about the current public Milestones
        Returns:
            json (dict)
        """
        url = DESTINY2_URL + 'Milestones/'
        return self._get_request(url)

    def get_groups_for_member(self, membership_type, membership_id):
        """Gets information about the groups an individual member has joined

        Args:
            membership_type (int):
                A valid non-BungieNet membership type (BungieMembershipType)
            membership_id (int):
                Destiny membership ID

        Returns:
            json(dict)
        """
        # /{membershipType}/{membershipId}/ | 0(NO FILTER)/1(CLANS)
        url = GROUP_URL + 'User/{}/{}/0/1/'
        url = url.format(membership_type, membership_id)
        return self._get_request(url)

    def get_weekly_milestones(self, group_id):
        """Gets the weekly milestones for a clan
        Args:
            groupId (int):
                The groupId of clan.
        returns json(dict)
        """
        # /Clan/{groupId}/WeeklyRewardState/
        url = DESTINY2_URL + 'Clan/{}/WeeklyRewardState/'.format(group_id)
        # using the returned json
        return self._get_request(url)

    def get_milestone_definitions(self, milestone_hash):
        """Gets the milestones definition for a given milestoneHash

        Args:
            milestone_hash (int):
                The hash value that represents the milestone within the manifest

        returns json(dict)
        """
        # /Manifest/DestinyMilestoneDefinition/{milestoneHash}
        url = DESTINY2_URL + 'Manifest/DestinyMilestoneDefinition/{}'.format(milestone_hash)
        return self._get_request(url)