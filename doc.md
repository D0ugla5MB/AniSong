# AniSong Project

**The project aims to streamline the creation of playlists for anime songs, automating the search, filtering, and addition of songs to playlists.**

## Project Scope Statement

The AniSong Project aims to automate the creation of anime song playlists by integrating web scraping, third-party music platform APIs, and a robust search/filter system. The project will focus on the following deliverables and functionalities:

### Technical Specifications

- **Backend:** Python 3.13.5, Django 5.2.4, BeautifulSoup (web scraping)
- **Frontend:** Vanilla JS, Django HTMX, AJAX (TBD)
- **Deployment:** Debian 12, Hostinger VPS, Nginx 1.24.x+
- **Supported Music Platforms:** Spotify, YouTube Music, (future: Apple Music, Amazon Music, Deezer)
- **Soundtrack Sources:** myanimelist (primary), anilist, kitsu

### Deliverables

1. **Search Engine:**  
   - Search by anime name, song name, artist name, or franchise name.
   - Real-time suggestions while typing, showing full result cards (anime name, song type, title, cover art, artist, interactive options).
   - Display mimics Spotify desktop artist/album view.
2. **Filtering Options:**  
   - Filter by song type (opening, ending, insert, ost).
   - (Future) Filter by season, year, genre.
3. **Playlist Automation:**  
   - Create playlists directly in user's preferred music service (Spotify, YouTube Music, etc.).
   - Direct Add (DaD) feature: add playlists without authentication, subject to platform API policies.
4. **Interactive Playlist Preview:**  
   - Preview, add, exclude, reorder tracks, delete playlist before finalizing.
5. **User Authentication:**  
   - Secure login and music platform linking, following API guidelines.
6. **User Login System:**  
   - Save/manage playlists, search history.
7. **User Feedback:**  
   - Users can report inaccurate song data or request revisions via feedback options.

### Constraints

- Adhere to authentication and API usage guidelines of supported music services.
- Prioritize desktop web experience.

### Assumptions

- Users have active accounts on their preferred music services.
- APIs for supported platforms remain accessible and functional.

### Out of Scope

- Standalone music streaming service.
- Mobile experience.

### Optional Features (Future Scope)

- Additional filters: genre, release year, season.
- Sorting: popularity, release date, alphabetical, etc
- Support for more music platforms.
- Compact view for search results.

## Functional Requirements

1. **Search Engine:**
   - Search by anime/song/artist/franchise.
   - Real-time, full-result suggestions.
   - Result card includes: anime name, song type, title, cover art, artist, add/preview options.
2. **Filtering Options:**
   - Filter by song type (opening, ending, insert, ost).
   - (Future) Filter by season, year.
3. **Playlist Automation:**
   - Create playlists in Spotify, YouTube Music, etc.
   - Direct Add (DaD) feature (subject to API feasibility).
4. **Interactive Playlist Preview:**
   - View, add, reorder, delete tracks/playlists before finalizing.
5. **User Authentication:**
   - Secure login and music platform linking.
6. **User Login System:**
   - Account creation, persistent playlists, search history.
7. **User Feedback:**
   - Report inaccurate data, request revisions, suggestions.

## Non-Functional Requirements

1. **Performance:**  
   - Search results within 1 second; playlist creation within 3 seconds.
2. **Scalability:**  
   - Minimal support scalable concurrent users.
3. **Security:**  
   - Secure storage and transmission (encryption).
4. **Usability:**  
   - Intuitive, desktop-focused UI; clear error messages.
5. **Reliability:**  
   - 99% uptime.
6. **Maintainability:**  
   - Clean, well-documented codebase.
7. **Compatibility:**  
   - Support major browsers (Chrome, Firefox, Edge).
8. **API Compliance:**  
   - Follow authentication and API guidelines.

## Data Structures

See [Data and Data Structures](.doc.sketch.ds.md) for full details. Key models:

- **User Account:**  
  - `username`, `password` (hashed), playlists, search history.
- **Playlist:**  
  - `playlist_id`, artist, songs (name, cover, duration).
- **Song:**  
  - `id`, anime (id, name), artist (id, name), index, cover, title, type, platform links.
- **Platform:**  
  - `platform_id`, name, song count, last updated.
- **SongPlatformAvailability:**  
  - `platform_availability` (binary string), `song_id`.
- **Anime:**  
  - `anime_id`, title, url, season, year, source.
- **Feedback:**  
  - `feedback_id`, `user_id`, `anime_id`, `song_id`, type, content, timestamp, status.

## Extraction Logic & Automation

- **Webscraping:**  
  - Extract anime/soundtrack data from myanimelist, anilist, kitsu.
  - Use anchor patterns, theme song divs, and input tags for platform links.
  - Scripts for duplicate checking, failed pattern handling, and environment variable updates (e.g., limits, year/season counts).
- **Automation:**  
  - Periodic scripts to validate limits, anchor counts, and year/season ranges.
  - Data integrity scripts to ensure unique entries and handle extraction failures.

## User Feedback Strategies

- Button for reporting inaccurate results.
- Manual input for revision/suggestion.
- Selection-based feedback (choose song, info to revise, send for review).

## References

- See [.doc.sketch.ds.md](.doc.sketch.ds.md) for all data models and field definitions.
- See [.doc.sketch.md](.doc.sketch.md) for extraction logic, automation, and implementation priorities.
