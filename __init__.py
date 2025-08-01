"""Here is the adjusted project guide, updated to exclusively use **Fetching Anime URLs (Option 2: Anime Seasons)** as the primary data acquisition strategy.

---
## Project Guide: Automated Anime Music Playlist Creator

This project aims to develop a tool that streamlines the creation of anime music playlists directly on various music platforms.

### 1. Core Idea
The main idea is to automate the process of creating playlists composed of anime-related music (openings, endings, insert songs, and original soundtracks). These playlists will then be generated directly on selected music streaming platforms.

### 2. Target Platforms
The primary focus will be on **Spotify** and **YouTube/YouTube Music**. However, the system must be designed to allow for easy future integration with other platforms such as Apple Music, Amazon Music, Deezer, and more.

### 3. Client-Side Workflow
The user experience on the client side will follow these steps:

1.  **Search for an Anime:** The user will input the name of a specific anime.
2.  **Suggestions:** There will be real-time suggestions while the user is typing. The user can select one of the suggestions, which will trigger a search.
Of course. Here is the adjusted section, incorporating the Spotify artist grid view as the general display concept.

---
### 3. Display Search Results
The system will display all possible matches for the provided anime title or indicate if no matches are found.

#### General Display Concept: Spotify-Style Grid 
The primary visual approach for displaying search results will be inspired by **Spotify's modern artist grid view**. This design is clean, highly visual, and allows users to quickly identify anime by their cover art.

* **Layout:** Results are arranged in a clean, responsive grid.
* **Card Design:** Each result is a card featuring:
    * A **prominent circular or rounded-square image** (the anime's poster).
    * The **anime's title** displayed clearly below the image.
    * A smaller sub-text indicating the format (e.g., **'TV', 'Movie', 'OVA'**).

#### Specific Implementations and Features

* **View Toggle:** While the grid is the default, the UI should include a **toggle button** allowing users to switch to a **Compact List View**. This text-focused layout is ideal for quickly scanning a large number of results.
* **Grouping Logic:** For searches that return many related entries (e.g., "Monogatari"), the grid or list can be organized with **Franchise Headings** to group related series, movies, and OVAs together.
* **"No Results" Handling:** When no matches are found, the system should provide a helpful response instead of a blank page. This can include:
    * A simple "No results found" message.
    * A "Did you mean...?" suggestion to correct potential typos.
    * A list of currently popular or trending anime to re-engage the user.
4.  **Filter Options:** Users can refine their search by defining the song type (e.g., opening, ending, insert song, original soundtrack).
5.  **Selection of Tracks:** From the returned results, users can select any number of tracks.
6.  **Playlist Preview:** Before final generation, users can preview the playlist.
7.  **Generate and View Playlist:** After review, the user can select their desired music platform. The tool will then generate the playlist on that platform.

### 4. Data Acquisition and Database Strategy

### 4.1. Primary Scraping Strategy: Anime Seasons
This method ensures a complete and exhaustive collection of anime by scraping data based on specific release seasons and years. This can be implemented in one of two ways.

* **4.1.1. Option A: Archive Page Scraping**
    1.  Access `https://myanimelist.net/anime/season/archive`.
    2.  Fetch all listed year/season combinations from the table elements on the page.
    3.  As a verification or loop control method, the total number of season URLs to be generated can be estimated. The formula would be roughly `(current_year - oldest_year + 1) * 4`. For example, if the archive runs from 1917 to 2025, you'd expect over 400 unique seasonal pages. This calculation helps validate that the scraper is finding all expected links.
    4.  Access each individual season/year URL (e.g., `https://myanimelist.net/anime/season/<year>/<season>`) to fetch the anime URLs on that page.

* **4.1.2. Option B: Direct Seasonal Access**
    1.  Directly access URLs in the format `https://myanimelist.net/anime/season/<year>/<season>`.
    2.  Loop through years (from 1917 to current) and seasons (fall, summer, spring, winter), generating each URL directly.
    3.  Continue fetching until no anchor tags with the class `link-title` are found on a page, indicating the end of listings for that season/year.
    
#### 4.2. Anime URL and Data Parsing
For both options, the scraped HTML pages will be parsed to extract anime details.

* **HTML Element Filters:** The process will focus on identifying `<a>` (anchor) tags with the class `link-title`.
* **Data Extraction:** From each identified tag, the `href` attribute (URL) and the `innerText` value (title) will be extracted.
* **URL Pattern:** Anime URLs (`https://myanimelist.net/anime/<id>/<name>`) will be parsed to extract:
    * `anime_id`: The unique numerical identifier.
    * `anime_name`: The primary title of the anime.
    * `anime_full_url`: The complete URL.
    * `anime_season` and `anime_start_year`: This contextual data **will be captured** from the seasonal URL that is being scraped.
* **Buffering:** Extracted data will be temporarily stored in a buffer before further processing.

#### 4.3. Soundtrack Fetching
Once individual anime URLs are processed, the next step is to extract opening and ending theme songs.

* **Target Elements:** Identify and save the two main `div` elements by their class names:
    * `op = theme-songs js-theme-songs opnening` (for openings)
    * `ed = theme-songs js-theme-songs ending` (for endings)
* **Data Extraction:** For each `div`, extract the `innerText` from all `<td>` tags with the attribute `width="84%"`.
* **Association:** The extracted song text will be connected with its corresponding `anime_id`. The data will be tagged with the `anime_season` and `anime_start_year` to ensure rich contextual data and filtering capabilities.

#### 4.4. Data Cleaning and Structuring
The raw `innerText` from soundtracks needs to be parsed into a structured format.

* **Desired Data Structure:** Each song entry should ideally conform to:
    `[song_number, song_name, artist_name, flavor_artist (optional)]`
    *(Note: If `song_number` is not explicitly found, it must default to `1`.)*
* **Combined Structure:** The final cleaned data for each song will be:
    `[handled_innerText, anime_name OR anime_id, song_type, song_unique_id, platform_id]`

#### 4.5. Music Platform API Fetching
Using the cleaned song data, the system will query music streaming platform APIs to find corresponding tracks and retrieve the following:

* `music_existence`: A boolean indicating if the song was found.
* `redirect_url`: The URL to the track on the respective platform.
* `thumbnail_image`: A URL to the track's album art or video thumbnail.

#### 4.6. Music Verification and Manual Checking
A manual verification process will likely be required to confirm the accuracy of matched songs, accounting for naming variations (Japanese vs. Roman characters) and availability. This could be an internal tool for data curation.

#### 4.7. Database Building
The database will be built with the verified data.

* **Initial Structure:** A single table (or collection) per music platform.
* **Target Platforms:** Spotify, YouTube Music, and potentially YouTube.
* **Future Platforms:** Apple Music, Deezer, Amazon Music.

### 5. Search and Filtering Logic
The client-side search will query the built database.

* **Real-time Suggestions:** Provide real-time suggestions for anime titles, song titles, and artist names.
* **Filter Options:**
    * **Fundamental Filters:** `opening`, `ending`, `other` (for insert songs/OSTs).
    * **Interesting Filters:** `year`, `season`, `genre`.

### 6. Playlist Generation
From the search results, the user can select any number of tracks to include in their playlist.

### 7. User Authentication
The system will implement secure API authentication (e.g., OAuth 2.0) for each music platform to add generated playlists to a user's account.

---
### **Appendix: Alternative Fetching Strategy for Updates**

While the seasonal scraping method is best for the initial, comprehensive database build, an alternative strategy was considered and is better suited for frequent, small updates.

**Fetching Anime URLs (Top Anime)**

This approach focuses on active and popular series by leveraging the https://myanimelist.net/topanime.php route.

Parameters: The data can be scraped using query parameters type and limit.

type: Possible values include airing, upcoming, tv, movie, ova, ona, special, bypopularity, favorite. Any other value defaults to the general top anime list. For this project, we'll focus on airing, upcoming, tv, movie, ova, ona, special.

limit: This parameter determines the starting index of the returned list, with each page returning 50 anime URLs.

A limit of 0 returns anime from index 1-50.

A limit of 50 returns anime from index 51-100.

A limit of 13 returns anime from index 14-63.

The default limit value is 0.

The order of type and limit in the URL does not matter.

Dynamic Range Discovery: Since it's not possible to load all options on a single page, and each page returns 50 elements, the scraping process will dynamically discover the total number of available entries for a given type. This involves:

Starting with a limit of 0 (or 50 as a starting point for subsequent pages).

Incrementing the limit value (e.g., by 500 initially, then by smaller increments) and checking the HTTP status code (200 for success, 404 for not found).

Once a 404 is encountered, a binary search-like approach will be used to pinpoint the exact maximum limit value that returns a 200 status, effectively finding the total number of entries. This ensures all possible pages are scraped.

"""