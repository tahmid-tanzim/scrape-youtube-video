import React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";

export default function Video({ videos }) {
  const openYouTube = video_id => {
    const url = `https://www.youtube.com/watch?v=${video_id}`;
    window.open(url, "_blank", "noopener,noreferrer");
  };

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell>Video Title</TableCell>
            <TableCell align="center">Video ID</TableCell>
            <TableCell align="right">Performance Score</TableCell>
            <TableCell align="right">Views</TableCell>
            <TableCell align="right">Likes</TableCell>
            <TableCell align="left">Channel</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {videos.map((video) => (
            <TableRow
              key={video.id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {video.title}
              </TableCell>
              <TableCell align="center">
                <Button
                  variant="text"
                  onClick={() => openYouTube(video.video_id)}
                >
                  {video.video_id}
                </Button>
              </TableCell>
              <TableCell align="right">
                {video.performance_score.toFixed(2)}
              </TableCell>
              <TableCell align="right">{video.view_count}</TableCell>
              <TableCell align="right">{video.like_count}</TableCell>
              <TableCell align="left">{video.channel.title}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
