import React from "react";
import axios from "axios";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import Select from "@mui/material/Select";
import Alert from "@mui/material/Alert";

import Header from "./components/Header";
import Video from "./components/Video";

function App() {
  const [tags, setTags] = React.useState("");
  const [scoreOrder, setScoreOrder] = React.useState("DESC");
  const [videoList, setVideoList] = React.useState([]);
  const [tagList, setTagList] = React.useState([]);

  const handleSearch = async () => {
    const responseVideos = await axios.get(
      `http://localhost:8000/api/videos?score_order=${scoreOrder}&tags=${tags}`
    );
    setVideoList(responseVideos.data);
  };

  React.useEffect(() => {
    (async () => {
      const responseTags = await axios.get("http://localhost:8000/api/tags");
      setTagList(responseTags.data);

      const responseVideos = await axios.get(
        "http://localhost:8000/api/videos?score_order=DESC"
      );
      setVideoList(responseVideos.data);
    })();
  }, []);

  return (
    <React.Fragment>
      <CssBaseline />
      <Container fixed>
        <Header />
        <Box sx={{ p: 2 }} />
        <Grid container spacing={2}>
          <Grid item xs={5}>
            <FormControl fullWidth>
              <InputLabel id="tags-select-label">Tags</InputLabel>
              <Select
                labelId="tags-select-label"
                id="tags-select"
                value={tags}
                label="Tags"
                onChange={(e) => setTags(e.target.value)}
              >
                <MenuItem value="">
                  <em>Select</em>
                </MenuItem>
                {tagList.map((tag) => (
                  <MenuItem key={tag.id} value={tag.id}>
                    {tag.value}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={5}>
            <FormControl fullWidth>
              <InputLabel id="score-select-label">Performance Score</InputLabel>
              <Select
                labelId="score-select-label"
                id="score-select"
                value={scoreOrder}
                label="Performance Score"
                onChange={(e) => setScoreOrder(e.target.value)}
              >
                <MenuItem value={"ASC"}>Ascending Order</MenuItem>
                <MenuItem value={"DESC"}>Descending Order</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={2}>
            <Button variant="contained" size="large" onClick={handleSearch}>
              Search
            </Button>
          </Grid>
        </Grid>
        <Box sx={{ p: 1 }} />
        {videoList.length > 0 && <Video videos={videoList} />}
        {videoList.length === 0 && (
          <Alert severity="info">No videos available!</Alert>
        )}
      </Container>
    </React.Fragment>
  );
}

export default App;
