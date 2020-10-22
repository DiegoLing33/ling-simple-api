
## 0.0.2 - 2020-10-22

### Added
- `state` column in `CoreModel` now works properly. When Remove action calls, 
state changes to `0` value. It means that object is removed. Get and List actions 
don't return rows with zero state.
- `POST /meta/{field}/remove` - removes the meta value
- `POST /meta/{field}/recover` - recovers the meta value
